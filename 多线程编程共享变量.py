# -*- coding: utf-8 -*-
from threading import  Thread
a=[1,23,4,5,6]
def addA1(lista):
    assert isinstance(lista,list)
    lista.append(12)
    print(lista)
def addA2(lista):
    assert isinstance(lista,list)
    lista.append(12)
    print(lista)
if __name__=='__main__':
    for i in range(12):
        t=Thread(target=addA1,args=(a,))
        t.start()
        t=Thread(target=addA2,args=(a,))
        t.start()