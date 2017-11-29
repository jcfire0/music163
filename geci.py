import requests
import re
from gequ import main
import os

idd=main.idd
k=len(idd)
f=open('song.txt','a')
for i in range(k):
    url='http://music.163.com/api/song/lyric?os=pc&id='+str(idd[i])+'&lv=-1&kv=-1&tv=-1'
    req=requests.get(url)           #抓取歌词的API
    data=req.json()
    r=data['lrc']['lyric']
    rr=re.compile('\[(.*?)\]')
    f.write(re.sub(rr,'',r).decode('utf-8'))
f.close()
