# -*- coding: utf-8 -*-
def makeStrong(func):
    def wapper():
        print("make stronging...")
        return "<strong>"+func()+"</strong>"
    return wapper
def makeP(func):
    def wapper():
        print("make bing...")
        return "<p>"+func()+"</p>"
    return wapper
@makeStrong
@makeP
def make():
    print("make ing....")
    return "hello world make"
res=make()
print(res)
'''
make stronging...
make bing...
make ing....
<strong><p>hello world make</p></strong>
'''