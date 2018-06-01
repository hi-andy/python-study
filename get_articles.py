import datetime
import re

import MySQLdb
import bs4
import requests

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1))
yesterday = yesterday.strftime("%Y-%m-%d %H:%M:%S")

# print(yesterday)

main_url = 'https://mp.weixin.qq.com/s/cf1qc0qfeivEBPGIAmsaGA'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}


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
    # body = soup.select('div#js_content')
    # body = soup.find_all("div", attrs={"class": "rich_media_content"}) # get list
    # body = soup.find_all("div", class_="rich_media_content")
    # body = re.sub('^(\s+?)', '', str(soup.find_all("div", class_="rich_media_content")[0]))

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

        body += str(line) + '\n'

    body = body.strip()

    article = (title, body, author, publish_time, article_url)
    return article


'''
输出文章
@out_type 输出类型：txt文本 db数据库；默认为 html
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
        for url in urls:
            article = get_article_data(url)

            with open('article.html', 'w') as f:
                f.write('<!DOCTYPE html>\n\
<html>\n\
<head>\n\
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n\
<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=0,viewport-fit=cover">\n\
<meta name="apple-mobile-web-app-capable" content="yes">\n\
<meta name="apple-mobile-web-app-status-bar-style" content="black">\n\
<meta name="format-detection" content="telephone=no">\n\
<title>%s</title>\n\
</head>\n\
<body>' % str(article[0]))
                f.write('<h2>%s</h2>' % str(article[0]) + '\n')
                f.write(str(article[1]) + '\n')
                f.write('</body>\n</html>\n')
            break


all_urls = get_articles_urls(main_url)
out_articles(all_urls)
