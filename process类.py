# -*- coding: utf-8 -*-
from multiprocessing import Process
import time
def gogogo():
    while True:
            print("子进程。。。。")
            time.sleep(1)
if __name__=='__main__':
    p = Process(target=gogogo)
    p.start()  # 让进程开始执行函数里的方法
    while True:
        time.sleep(1)
        p.join()#等待子进程执行完成才向下执行
        print("父进程。。。。")
