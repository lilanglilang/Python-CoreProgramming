# -*- coding: utf-8 -*-
import os
import time
num=100
ret=os.fork()
if ret==0:
    print("child is running....")
    num=num+1
    print("num is %s"%num)
else:
    time.sleep(3)
    print("parent is running....")
    print("num is %s" % num)
#输出结果是101 和100 进程之间的变量互不影响
