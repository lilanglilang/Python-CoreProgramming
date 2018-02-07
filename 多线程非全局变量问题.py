# -*- coding: utf-8 -*-
from threading import Thread
import threading
import time
def getTest():
    name=threading.current_thread().name
    print("---thread name---%s"%(name,))
    g_num=0
    if name=='Thread-1':
        g_num=g_num+1
    else:
        time.sleep(2)
    print("---thread name---%s   %s"%(name,g_num))
if __name__=='__main__':
    p2 = Thread(target=getTest)
    p2.start()
    p1 = Thread(target=getTest)
    p1.start()
'''
充分说明了多线程函数类的变量是不会发生共享的，只有全局变量会发生共享
---thread name---Thread-1
---thread name---Thread-1   1
---thread name---Thread-2
---thread name---Thread-2   0
'''


