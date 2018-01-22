# -*- coding: utf-8 -*-
def hello(func):
    def wapper(a,b):
         return func(a,b)
    return wapper
@hello
def hehe(a,b):
    print(a+b)
print(hehe(1,2))
'''
3
None
'''

def hello(func):
    return func
@hello
def hehe(a,b):
    print(a+b)
print(hehe(1,2))
'''
3
None
'''
