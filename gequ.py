import requests
from bs4 import BeautifulSoup
import re


def geturl(url):
        try:
                url='http://music.163.com/playlist?id=908021904'
                header={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding':'gzip, deflate',
                        'Accept-Language':'zh-CN,zh;q=0.8',
                        'Connection':'keep-alive',
                        'Host':'music.163.com',
                        'Referer':'http://music.163.com/',
                        'Upgrade-Insecure-Requests':'1',
                        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
                r=requests.get(url,headers=header)
                html=r.text
                return html                                  #通过对requests中加header操作，获取歌单界面的源代码中所没有的歌曲id
        except:
                print u'歌曲ID获取失败'
              

def gequ(html):
	soup=BeautifulSoup(html,'html.parser')
	r=soup.find_all('ul',class_="f-hide")
	rr=str(r)
	q=re.compile('id=(.*?)"')
	idd=re.findall(q,rr)
	return idd                              #获取歌曲id，放进一个列表中

class main():
	url='http://music.163.com/playlist?id=908021904'
	html=geturl(url)
	idd=gequ(html)
	
