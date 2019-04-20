#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 20:20
# @Author  : Zhnag Dongdong  
# @File    : function.py
def print_sym(sym,count):
    print(sym * count)
def print_msg(msg):
    print('\033[045m%s\033[0m' % msg)

print(print_sym)
print(print_msg)  # 打印函数名就打印出其对应的内存地址
print_sym('=',30)
print_msg('hello world')
print_sym('=',30)

def max2(x,y):
    if x>=y:
        return(x)
    else:
        return(y)
max2(100,101)

def interact():
    name = input('username>>:\n').strip()
    pwd = input('password>>:\n').strip()
    print(name,pwd)
# interact()

def auth(username, password):
    """

    :param username:
    :param password:
    :return:
    """
def put():
    """

    :return:
    """
def get():
    """

    :return:
    """

def foo():
    print('from foo')
    bar()

def bar():
    print('from bar')

foo()


res = max2(10,3)
print(res)
print(max2(max2(2,10),11))

def func():
    pass
def func1():
    return
def func2():
    return None

print(func())
print(func1())
print(func2())

def func3():
    return 2
def func4():
    return 1,2,3,[1,2,3]
print(func3())
print(func4())
func3()
func4()
max2(10,3)
a = 3
a  # 这几句没有任何返回，这说明函数本质上就是变量，直接输入变量是不会有直接打印的，除非使用print()

print('我是一条分隔线'.center(40,'-'))
def foo(x, y, z):
    print(x, y, z)
foo(1,2,3)
foo(z=1,x=2,y=3)  # 位置实参
foo(1,z=2,y=3)  # 位置实参与关键字实参可以混合使用，但位置实参必须放在前面

def register(name, age, sex='male'):
    return name,age,sex
print(register('Albert',18))
print(register('James',20,'female'))

print('我是一条分隔线'.center(40,'-'))
def foo(x,y,*args):
    print(x,y,args)
print(foo(1,2,3,4,5,6,7))
print(foo(1,2,*'hello'))  # 将字符川打散
print(foo(1,2,'hello'))
print(foo(1,2,*[3,4,5,6]))  # 将列表打散
print(foo(1,2,[2,3,4,5,6]))
print(foo(*[1,2,3,4]))
print(foo(1,2,3,4))
print(foo(*[1,2]))

def foo(x,y,z,**kwargs):
    print(x,y,z,kwargs)
print(foo(1,y=2,z=3,a=1,b=2,c=3))
print(foo(1,2,3,**{'a':1,'b':2}))  # 这里是说，一开始是个字典是不能作为元素输入的，但打散之后就可以了

print('我是一条分隔线'.center(40,'-'))
def index(name,age,gender):
    print('welcome %s %s %s' % (name,age,gender))

def foo(x,y):
    print(x,y)
def wrapper(*args,**kwargs):
    print(args,kwargs)
    foo(*args, **kwargs)

wrapper(2,3)

def foo(x,y,*args,a=1,b,**kwargs):
    print(x,y,args,a,b,kwargs)

foo(1,2,3,4,5,b=3,c=4,d=5)

def auth(name, pwd, **kwargs):
    print(name)
    print(pwd)
    print(kwargs)

auth(name='Albert', pwd='123')
auth(name='Albert', pwd='123', group='group1')