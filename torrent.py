#!/usr/bin/env python
import libtorrent as lt
import sys
from bencode import *
from hashlib import *
import random


with open(sys.argv[1],'rb') as FileHandle,\
    open('sha1EncodeRename.torrent','wb') as reWrite:
        decodeFileHandle=bdecode(FileHandle.read())
        arrayPoint=['path.utf-8','path']
        for i in decodeFileHandle['info']['files']:
           for j in arrayPoint:
               try:
                   i[j][0]=sha1(i[j][0].split('.')[0]).hexdigest()+'.'+i[j][0].split('.')[-1]
               except:
                   continue
           print i['path'][0]

        reWrite.write(bencode(decodeFileHandle))


