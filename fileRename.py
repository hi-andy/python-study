#!/bin/python env
# 文件重命名程序

import os
import re

# 存放文件目录
filedir = './mp3/'
# path = input('请输入文件路径:')

files = os.listdir(filedir)
addstring = ''

for file in files:
    if not os.path.isdir(file):
        m = re.match(r'(.{2})(\d{3,}).*(\.mp3)$', file)
        if str(m) != 'None':
            newName = m.group(2) + '.' + m.group(1) + m.group(3)
            # print(newName)
            os.rename(filedir + file, filedir + newName)
            print(filedir + file, filedir + newName)
