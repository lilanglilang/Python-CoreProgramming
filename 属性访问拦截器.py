# -*- coding: utf-8 -*-
class Demo(object):
    def __init__(self):
        self.python=0
    def __getattribute__(self, item):
        if item=='python':
            print("hello，man")

        else:
            return object.__getattribute__(self,item)
dm=Demo()
dm.python