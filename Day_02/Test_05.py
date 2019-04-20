#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 14:28
# @Author  : Zhnag Dongdong  
# @File    : Test_05.py
input_user_name = str(input('请输入用户名：'))
if input_user_name == 'Albert':
    input_key = str(input('请输入密码：'))
    if input_key == '1':
        print('用户名和密码输入正确，您已成功登录！')
    else:
        print('密码输入错误')
else:
    print('用户名输入错误')
