# -*- coding: utf-8 -*-
def func1(func):
    def inner():
        print("func1正在执行")
        func()
    return inner
def func2():
    print("func2正在执行")
def func3():
    print("func3正在执行")
func2=func1(func2)
func2()
func2()
'''
func1正在执行
func2正在执行
func1正在执行
func2正在执行
'''


def func1(func):
    def inner():
        print("func1正在执行")
        func()
    return inner
@func1
def func2():
    print("func2正在执行")
@func1
def func3():
    print("func3正在执行")

func2()
func2()
'''
func1正在执行
func2正在执行
func1正在执行
func2正在执行
'''
