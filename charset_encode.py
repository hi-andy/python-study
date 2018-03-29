import sys

unicode = '你好'

gbk = unicode.encode('gbk')
utf8 = unicode.encode('utf8')
gb2312 = unicode.encode('gb2312')

print('GBK:', gbk)
print('UTF8:', utf8)
print('GB2313:', gb2312)

gbk_unicode = gbk.decode('gbk')
utf8_unicode = utf8.decode('utf8')
gb2312_unicode = gbk.decode('gb2312')


print(gbk_unicode, utf8_unicode, gb2312_unicode)


