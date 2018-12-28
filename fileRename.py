#!/bin/python env
# 文件重命名程序

import os
import re

# 存放文件目录
file_dir = './mp3/'
# path = input('请输入文件路径:')

files = os.listdir(file_dir)
add_string = ''

for file in files:
    if not os.path.isdir(file):
        m = re.match(r'(.{2})(\d{3,}).*(\.mp3)$', file)
        if str(m) != 'None':
            newName = m.group(2) + '.' + m.group(1) + m.group(3)
            # print(newName)
            # os.rename(file_dir + file, file_dir + newName)
            print(file_dir + file, file_dir + newName)
