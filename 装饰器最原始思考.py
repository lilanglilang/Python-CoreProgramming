# -*- coding: utf-8 -*-
def hello(func):
    def wapper():
         return func()
    return wapper
@hello
def hehe():
    return "nihao"
print(hehe())