# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os
import random
import time
def work(num):
    for i in range(5):
        print("==pid==%d==num==%d="%(os.getpid(),num))
        time.sleep(2)
if __name__=='__main__':
    p=Pool(4)
    for i in range(10):
        print("-----%d----"%i)
        p.apply_async(work,(i,))
    p.close()
    p.join()#没有这个的话，进程池中的任务很有可能不会执行

