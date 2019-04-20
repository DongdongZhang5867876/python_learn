#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 11:13
# @Author  : Zhnag Dongdong
# @File    : test_03.py
for i in range(1,10):  # 打印九九乘法表
    for j in range(1,i+1):
        print('%d × %d = %d  '%(j,i,i*j),end='')
    print('\n')