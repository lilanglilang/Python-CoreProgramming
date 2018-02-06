# -*- coding: utf-8 -*-
#多个线程执行同一个函数，互不影响
#线程之间共享全局变量
from threading import Thread
import time
import os
def sayHello():
    print("%s我正在执行"%(Thread.name))

def TreadRun():
    for i in range(10):
        t=Thread(target=sayHello)
        t.start()
if __name__=='__main__':
    TreadRun()
    print("子线程执行结束")