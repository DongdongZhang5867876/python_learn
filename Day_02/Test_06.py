#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 14:47
# @Author  : Zhnag Dongdong  
# @File    : Test_06.py
dict_user_log_in = {'Albert':'超级管理员','tom':'普通管理员','jack':'业务主管','rain':'业务主管'}
input_user_name = input('请输入用户名：').lower()
if input_user_name in dict_user_log_in:
    print('您的权限是：%s'%dict_user_log_in[input_user_name])
else:
    print('您的权限是：普通用户')