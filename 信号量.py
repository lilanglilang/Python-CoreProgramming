# -*- coding: utf-8 -*-
'''
每当调用acquire()时，内置计数器-1
每当调用release()时，内置计数器+1
计数器不能小于0，当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
'''
import time
import threading

SEMAPHORE = threading.Semaphore(5)
s1= SEMAPHORE  #添加一个计数器

def foo():
    s1.acquire()    #计数器获得锁

    time.sleep(2)   #程序休眠2秒
    print("ok",time.ctime())
    s1.release()    #计数器释放锁


for i in range(20):
    t1=threading.Thread(target=foo,args=()) #创建线程
    t1.start()  #启动线程