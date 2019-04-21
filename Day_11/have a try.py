#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 19:25
# @Author  : Zhnag Dongdong  
# @File    : have a try.py
import time
time1 = time.time()
l1 = ['egg%s'%i for i in range(1000000)]
time2 = time.time()
print(time2-time1)

time3 = time.time()
li = []
for i in range(1000000):
    li.append('egg%s'%i)
time4 = time.time()
print(time4-time3)

li = ('egg%s'% i for i  in range(1000000) if i > 100000)
print(next(li))
print(next(li))