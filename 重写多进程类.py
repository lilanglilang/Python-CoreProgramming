# -*- coding: utf-8 -*-
from multiprocessing import Process
import time
class myProcess(Process):
    def run(self):
        print("hello")
        time.sleep(1)
if __name__=='__main__':
    p=myProcess()
    p.start()