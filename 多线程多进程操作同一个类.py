# -*- coding: utf-8 -*-
import time
import threading
from multiprocessing import Process
class hello():
    def __init__(self):
        self.num = 0

    def addNum(self):
            self.num += 1
            print(self.num)

if __name__ == '__main__':
    hel = hello()
    p1 = Process(target=hel.addNum(),name='p1')
    p2 = Process(target=hel.addNum(),name='p2')
    p1.start()
    p2.start()
    p1.join()
    p2.join()