#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 14:25
# @Author  : Zhnag Dongdong  
# @File    : Test_04.py
for i in range(1,10):  # 打印金字塔
    print(' ' * (9 - i),end='')
    print('金'*i,end='')
    print('\n')