# -*- coding: utf-8 -*-
from threading import Lock
from threading import Thread
num=0
def test1():
    global  num
    for i in range(10000000):
        mutex.acquire()
        num+=1
        mutex.release()
    print(num)
def test2():
    global num
    for i in range(10000000):
        mutex.acquire()
        num += 1
        mutex.release()
    print(num)
if __name__=='__main__':
  mutex=Lock()
  p1=Thread(target=test2)
  p2=Thread(target=test1)
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  print(num)