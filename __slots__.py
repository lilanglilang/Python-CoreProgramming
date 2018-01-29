# -*- coding: utf-8 -*-
#限制实例属性
#类属性不会限制
class mySlots(object):
    __slots__ = ('name','age')

world=mySlots
world.hehe=10
print(world.hehe)#10
hello=mySlots()

hello.hehe=10#产生异常