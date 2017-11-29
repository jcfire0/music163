import os

def baocun(yun,h):
   wenjian=yun+'.txt'
   f=open(wenjian,'a')
   f.write(h+'\n')
   f.close()
