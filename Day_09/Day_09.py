#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 10:23
# @Author  : Zhnag Dongdong  
# @File    : Day_09.py
def max2(x,y):
    if x > y:
        return x
    else:
        return y

def max3(x,y,z):
    res1 = max2(x,y)
    res2 = max2(res1,z)
    return res2

print(max3(11,19,21))

def func1():
    print('func1')
    def func2():
        print('func2')
    print(func2())
    func2()
func1()
# func2()  会报错

def f1():
    print('f1')
    def f2():
        print('f2')
        def f3():
            print('f3')
        f3()
    f2()  # 在同级定义就必须在同级调用，否则在上一级下一级都会报错！！！
f1()

global_count = 0
def global_check():
    print(global_count)

def global_modify():
    global_count =1
    print(global_count)
global_check()
global_modify()
print(global_count)  # 意思是，虽然在函数内部对全局变量global_count进行了修改，但一旦出了函数它就立刻撤销所有修改

print('-'*60)
f0 = 0
def f1():
    # nonlocal f1
    f0 = 1
    print(f0)
    def f2():
        # nonlocal f1
        f0 = 3
        print(f0)
    f2()
    print(f0)
f1()
print(f0)

print('-'*60)
def bar():
    print('from bar')
f = bar()
f
g = bar
g()

def bar():
    print('from bar')
def wrapper(func):
    func()
wrapper(bar)

def bar():
    print('from bar')
def foo(func):
    return func
f = foo(bar)
f()
print('*'*30)
foo(bar)()
foo(bar())
def foo2():
    return print('from bar')
foo2()
print('-'*30)
def foo3():
    return bar()
foo3()

def get():
    print('from get')
def put():
    print('from put')
l1 = [get,put]
l1[1]()

print('-'*30)
def auth():
    print('登录。。。。。。。')
def register():
    print('注册。。。。。。。')
def check():
    print('查看。。。。。。。')
def transfer():
    print('转账。。。。。。。')
def pay():
    print('支付。。。。。。。')

func_dict = {
    '1':auth,
    '2':register,
    '3':check,
    '4':transfer,
    '5':pay
}
func_dict['1']()
func_dict['2']()

print('-'*60)
def outer():
    # def inner():
    #     print('inner 函数执行')
    # inner()
    def inner_2():
        print('inner 函数执行')
    return inner_2
f = outer()()
print(f)

print('以下是装饰器代码'.center(30,'-'))
# 无参装饰器实现过程
import time
def outer(func):
    def timer(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print(end - start)
        return res
    return timer
@outer  # index = outer(index)
def home(name):
    time.sleep(2)
    print('welcome %s to home page'%name)

@outer
def index():
    time.sleep(1)
    print('welcome to index page')
    return 123

index()
home('Albert')

# 用户认证装饰器
import time
current_user = {
    'username': None,
}

def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['username']:
            print('已经登陆过了')
            res = func(*args, **kwargs)
            return res

        name = input('用户名>>: ').strip()
        pwd = input('密码>>: ').strip()
        if name == 'Albert' and pwd == '1':
            print('登陆成功')
            current_user['username'] = name
            res = func(*args, **kwargs)
            return res
        else:
            print('用户名或密码错误')
    return wrapper

@auth
def index():
    time.sleep(1)
    print('welcome to index page')
    return 1
@auth
def home(name):
    time.sleep(2)
    print('welcome %s to home page' % name)

index()
home('Albert')
