# -*- coding: utf-8 -*-
from threading import Lock
from threading import Thread
num=0
def test1():
    global  num
    mutex.acquire()
    for i in range(100000000):
        num+=1
    mutex.release()

def test2():
    global num
    mutex.acquire()
    for i in range(100000000):
        num += 1
    mutex.release()
if __name__=='__main__':
  mutex=Lock()
  p1=Thread(target=test2)
  p2=Thread(target=test1)
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  print(num)