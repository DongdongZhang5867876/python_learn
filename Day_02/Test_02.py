#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 11:13
# @Author  : Zhnag Dongdong
# @File    : test_02.py
dict_user = {'张三':111111,'李四':222222,'王五':333333}
user_name = str(input('请输入你的名字：'))
true_key = dict_user[user_name]
input_key = int(input('请输入你的密码：'))
for i in range(2):
    if input_key == true_key:
        print('输入正确，你已经成功登录！')
        break
    else:
        input_key = input('输入错误，你还有%d次机会，请重新输入：'%(2-i))
else:
    print('你TM都输错三次了，不给你输了！！！')