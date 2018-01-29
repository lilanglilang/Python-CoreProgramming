# -*- coding: utf-8 -*-
'''
b=(for x in range(10))
#产生一个生成器对象
'''
'''
def run():
    for i in range(19):
        yield i
rn=run()
for x in rn:
    print(x)
def run():
    for i in range(19):
        temp=yield i
        print(temp)
        i=i+1
tt=run()
for x in tt:
    print(x)
'''
0
None
1
None
2
None
3
None
4
None
5
None
6
None
7
None
8
None
9
None
10
None
11
None
12
None
13
None
14
None
15
None
16
None
17
None
18
None
'''

'''
'''
def run():
    for i in range(19):
        temp=yield i
        print(temp)
        i=i+1
tt=run()
print(tt.__next__())
tt.send("haha")#也可以让暂停的地方继续执行
print(tt.__next__())

'''

'''
def run():
    for i in range(19):
        temp=yield i
        print(temp)
        i=i+1
tt=run()

tt.send("haha")#TypeError: can't send non-None value to a just-started generator
'''

def run():
    for i in range(19):
        temp= yield i
        print(temp)
        i=i+1
tt=run()


