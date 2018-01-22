# -*- coding: utf-8 -*-
def help(func):
    '''
    通用装饰器
    :param func:
    :return:
    '''
    def wapper(*args,**kwargs):
        func(args,kwargs)
    return wapper
def moreHelp(*args,**kwargs):
    '''
    超级通用装饰器
    :param args:
    :param kwargs:
    :return:
    '''
    def funcGet(func):
        def wapped(*args,**kwargs):
            func(*args,**kwargs)
        return  wapped
    return funcGet
@moreHelp()
def hehe(a,b):
    print(a+b)
hehe(1,2)
'''
3
'''

