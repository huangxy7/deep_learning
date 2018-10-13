#!/usr/bin/env python
#_*_coding=utf-8_*_

#########################
# >File Nime: rename.py
# >author: ly
# >email: 406728295@qq.com
#########################
import os

path='/home/jsj/Downloads/10000张/red/'    

#获取该目录下所有文件，存入列表中
f=os.listdir(path)
n=0
for i in f:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+f[n]
    
    #设置新文件名
    newname=path+'red_'+str(n+1)+'.jpg'
    
    #用os模块中的rename方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    
    n+=1
