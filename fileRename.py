#!/bin/python env
# 文件重命名程序

import os
import re

# 存放文件目录
filedir = '/Users/xxx/xxx'
#path = input('请输入文件路径:')

files = os.listdir(filedir)
addstring = '.封神榜.'

for file in files:
    if not os.path.isdir(file):
        #print(os.path.splittext(file))
        m = re.match(r'(\d{2}).*(mkv)$', file)
        newName = m.group(1) + addstring +  m.group(2)
        os.rename(filedir + file, filedir + newName)
        #print(filedir + file, filedir + newName)
