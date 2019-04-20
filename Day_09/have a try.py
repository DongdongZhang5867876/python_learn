#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 22:19
# @Author  : Zhnag Dongdong  
# @File    : have a try.py
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

