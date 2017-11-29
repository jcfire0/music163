from xpinyin import Pinyin
import re
import jieba
import os
from baocun import baocun




def yunmu():
   f=open('song.txt','r')
   lis=[]
   for eachline in f:
       seg=list(jieba.cut(eachline,cut_all=True))       #用结巴分词模块对song.txt中每行读取的歌词进行分词
       gg=len(seg)
       for i in range(0,gg):
           h=seg[i].decode('utf-8')
           q=Pinyin()           #获取分词后每个词组的拼音
           m=q.get_pinyin(h)
           p=re.compile('-')
           a=p.split(m)
           k=len(a)                       #获取最后一个字的拼音
           patten=re.compile('(a|o|e|i|u|v|ai|ei|ui|ao|ou|iv|ie|ve|er|an|en|in|un|vn|ang|eng|ing|ong|uan|ian|uang|iang|iong|ue)$')
           c=str(a[k-1])
           y=patten.search(c)
           if y:
              yun=str(y.group())
              baocun(yun,h)                 #提取出韵母，根据这个，调用函数baocun进行分类存储
   print u'完成'
   f.close()



    

class main():
    yunmu()
