import json
import os
import re

import requests

data = {}
if os.path.isfile('data.json'):
    with open('data.json', 'r') as f:
        data = json.load(f)
    previous_ver = data['kindle']
else:
    previous_ver = data['kindle'] = '0'

# 检查 Kindle 软件更新。
url = 'https://www.amazon.cn/gp/help/customer/display.html/ref=hp_left_v4_sib?ie=UTF8&nodeId=201756220'

r = requests.get(url)
m = re.search('.*[\u4e00-\u9fa5]+(\d\.\d?\.?\d\.?\d?)', r.text)

if str(m) != 'None':
    new_ver = m.group(1).replace('.', '')
    data['kindle'] = new_ver

    if int(new_ver) > int(previous_ver):
        print('Have new version!')

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
        outfile.write('\n')

print(type(data['kindle']))
