import chardet

unicode = '你好'

# print(chardet.detect(unicode))
# print(type(unicode))

gbk = unicode.encode('GBK')
# utf8 = unicode.encode('utf8')
# gb2312 = unicode.encode('gb2312')

print(type(gbk))
print(chardet.detect(gbk))

# print('GBK: ', gbk)
# print('UTF8: ', utf8)
# print('GB2313: ', gb2312)

# gbk_unicode = gbk.decode('gbk')
# utf8_unicode = utf8.decode('utf8')
# gb2312_unicode = gbk2312.decode('gb2312')

# print('GBK_UNICODE: %s \n' % gbk_unicode,'UTF8_UNICODE: %s\n' % utf8_unicode,'GB2312_UNICODE: %s\n' % gb2312_unicode)
"""
<class 'bytes'>
{'encoding': 'TIS-620', 'confidence': 0.3598212120361634, 'language': 'Thai'}
"""