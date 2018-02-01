# -*- coding: utf-8 -*-
class Test(object):
    def __init__(self,func):
        print("hello")
    def __call__(self, *args, **kwargs):
        print("python")
@Test
def test():
    print("hello")
test()
'''
hello
python
'''