import datetime
import os
import re

import MySQLdb
import bs4
import requests

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1))
yesterday = yesterday.strftime("%Y-%m-%d %H:%M:%S")

# print(yesterday)

main_url = 'https://mp.weixin.qq.com/s/cf1qc0qfeivEBPGIAmsaGA'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
}


def get_articles_urls(in_url):
    response = requests.get(in_url)
    soup = bs4.BeautifulSoup(response.text, "html5lib")
    return [a.attrs.get('href') for a in soup.select('ul.list-paddingleft-2 a[href^=http://mp.weixin.qq.com/s?]')]


def get_article_data(article_url):
    response = requests.get(article_url)
    soup = bs4.BeautifulSoup(response.text, "html5lib")

    # 删除看似无用的标签：section img
    [s.extract() for s in soup('section')]
    [s.extract() for s in soup('img')]

    # 匹配标题，去除首尾空白
    rough_title = soup.select('h2.rich_media_title')[0].get_text()
    js_title = re.sub('\s+', '', rough_title)
    title = re.match(r'.*document\.write\("(.*)"\);}$', js_title).group(1)
    # 匹配作者
    author = re.sub('\s+', '', soup.select('span#profileBt a')[0].get_text())
    # 发布时间
    publish_time = 000
    # body = soup.select('div.rich_media_content ')[0].get_text().strip()
    # body = soup.find_all("div", attrs={"class": "rich_media_content"}) # get list

    misc_body = soup.find_all("div", class_="rich_media_content")[0].contents

    # 文章主题. 去除空白行，并且拼接。
    body = ''
    for line in misc_body:
        tag = re.match('<p\s*.*?>(.*)?</p>', str(line))
        if str(tag) != 'None':
            if tag.group(1) == '<br/>' or tag.group(1) == '':
                continue
            else:
                tag2 = re.match('<span\s*.+?>(.*)?</span>', str(tag.group(1)))
                if str(tag2) != 'None':
                    if tag2.group(1) == '<br/>' or tag2.group(1) == '':
                        continue

        # 去除所有内联样式，原有样式在 Kindle 表现不佳。
        line = re.sub('\s*?style="\s*.+?"', '', str(line))
        body += str(line) + '\n'

    body = body.strip()

    article = (title, body, author, publish_time, article_url)
    return article


'''
输出文章
@out_type 输出类型：html文件 db数据库；默认为 html
'''


def out_articles(urls, out_type='html'):
    if out_type == 'db':
        db = MySQLdb.connect("localhost", "root", "", "weixin", charset='utf8mb4')
        cursor = db.cursor()
        for url in urls:
            values = [get_article_data(url)]
            sql = "INSERT INTO article(title, body, author, publish_time, url) VALUES(%s, %s, %s, %s, %s)"

            # sql = "INSERT INTO article(title, author) VALUES('test', 'andy')"
            # cursor.executemany(sql, values)
            # cursor.execute(sql)
            # db.commit()

            try:
                cursor.executemany(sql, values)
                db.commit()
            except:
                db.rollback()
            # break
        db.close()
    else:
        opf_item = ''
        opf_itemref = ''
        ncx_item = ''
        content_item = ''
        book_name = 'L先生说'

        path = './book/'
        if not os.path.exists(path):
            os.makedirs(path)

        for key, url in enumerate(urls):
            article = get_article_data(url)
            index = key + 1
            file_name = 'article%s' % index
            full_file_name = 'article%s.html' % index
            title = article[0]
            body = article[1]

            # 每篇文章，单独一个文件
            with open(path + full_file_name, 'w') as f:
                f.write('<!DOCTYPE html>\n\
<html xmlns="http://www.w3.org/1999/xhtml">\n\
<head>\n\
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n\
<title>{0}</title>\n\
</head>\n\
<body>\n\
    <h2>{1}</h2>\n\
    {2}\n\
</body>\n\
</html>\n'.format(title, title, body))

            # opf 文件列表
            opf_item += '\t<item id="{0}" media-type="text/x-oeb1-document" href="{1}"></item>'.format(file_name,
                                                                                                       full_file_name) + '\n'
            opf_itemref += '\t<itemref idref="%s"/>' % file_name + '\n'

            # 目录列表
            content_item += '\t\t<li><a href="{0}">{1}</a></li>'.format(full_file_name, title) + '\n'

            # ncx 列表
            ncx_item += '\t\t\t<navPoint id="navpoint-{0}" playOrder="{1}">\n\
                <navLabel>\n\
                    <text>{2}</text>\n\
                </navLabel>\n\
                <content src="{3}"/>\n\
            </navPoint>'.format((index + 1), (index + 1), title, full_file_name) + '\n'

        # 生成目录文件
        with open(path + 'toc.html', 'a') as f:
            f.write('<!DOCTYPE html>\n\
<html xmlns="http://www.w3.org/1999/xhtml">\n\
<head>\n\
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n\
<title>目录</title>\n\
</head>\n\
<body>\n\
<h1 id="toc">文章目录</h1>\n\
    <ul>\n\
        {0}\
    </ul>\n\
</body>\n\
</html>'.format(content_item))

        # 生成 ncx
        with open(path + 'toc.ncx', 'a') as f:
            f.write('<?xml version="1.0"　encoding="UTF-8"?>\n\
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">\n\
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n\
<head>\n\
</head>\n\
<docTitle>\n\
    <text>{0}</text>\n\
</docTitle>\n\
<navMap>\n\
    <navPoint id="navpoint-1" playOrder="1">\n\
        <navLabel>\n\
            <text>Content</text>\n\
        </navLabel>\n\
        <content src="toc.html#toc"/>\n\
    </navPoint>\n\
    {1}\
</navMap >\n\
</ncx>\n'.format(book_name, ncx_item))

        # 生成 opf 文件
        with open(path + 'book.opf', 'a') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n\
<package unique-identifier="uid" xmlns:opf="http://www.idpf.org/2007/opf" xmlns:asd="http://www.idpf.org/asdfaf">\n\
<metadata>\n\
    <dc-metadata  xmlns:dc="http://purl.org/metadata/dublin_core" xmlns:oebpackage="http://openebook.org/namespaces/oeb-package/1.0/">\n\
        <dc:Title>{0}</dc:Title>\n\
        <dc:Language>zh</dc:Language>\n\
        <dc:Creator>Andy</dc:Creator>\n\
        <dc:Copyrights>文章版本：归原作者所有</dc:Copyrights>\n\
        <dc:Publisher>Andy</dc:Publisher>\n\
        <x-metadata>\n\
            <EmbeddedCover>images/cover.jpg</EmbeddedCover>\n\
        </x-metadata>\n\
    </dc-metadata>\n\
</metadata>\n\
<manifest>\n\
    <item id="content" media-type="text/x-oeb1-document" href="toc.html"></item>\n\
    <item id="ncx" media-type="application/x-dtbncx+xml" href="toc.ncx"/>\n\
    {1}\n\
</manifest>\n\
<spine toc="ncx">\n\
    <itemref idref="content"/>\n\
    {2}\n\
</spine>\n\
<guide>\n\
    <reference type="toc" title="目录" href="toc.html"/>\n\
</guide>\n\
</package>'.format(book_name, opf_item, opf_itemref))

            # break


all_urls = get_articles_urls(main_url)
out_articles(all_urls)
