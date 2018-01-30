# -*- coding: utf-8 -*-
#此程序只能在Linux环境中使用
#父进程中中的ret值就是子进程返回来的pid值
import os
import time
ret=os.fork()
print(ret)
if ret>0:
    while True:
        print("*"*10)
        print("----父进程----%d"%os.getpid())
        print(ret)
        time.sleep(1)
else:
    while True:
        print("*" * 10)
        print("----子进程----%d--%d" % (os.getpid(),os.getppid()))
        time.sleep(1)
