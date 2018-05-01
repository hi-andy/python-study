#!/bin/python env
# 文件重命名程序

import os
import re

defaultPath = '/Users/hua/Downloads/封S榜/'
#path = input('请输入文件路径:')

files = os.listdir(defaultPath)
addstring = '.封神榜.'

for file in files:
    if not os.path.isdir(file):
        #print(os.path.splittext(file))
        m = re.match(r'(\d{2}).*(mkv)$', file)
        newName = m.group(1) + addstring +  m.group(2)
        os.rename(defaultPath + file, defaultPath + newName)
        #print(defaultPath + file, defaultPath + newName)
