#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 18:55
# @Author  : Zhnag Dongdong  
# @File    : Day_05_02.py
import sys
list_users = []
each_user = []
list_users_name = []
list_users_key = []
list_users_wage = []
list_forbid_user_name = []
with open('Users.txt','r',encoding='utf-8') as f:
    list_users = f.readlines()  # 一行行读取Users.txt文件，将每一行作为一个元素存入list_users列表
with open('Blacklist.txt','r',encoding='utf-8') as f:  # 读取黑名单里的用户名
    list_forbid_user_name = f.readlines()
for i in range(len(list_users)):  # 将list_users列表拆分成三个列表
    each_user = list_users[i].split('|')
    list_users_name.append(each_user[0])
    list_users_key.append(each_user[1])
    list_users_wage.append(int(each_user[2]))
user_name = input("用户名：\n")
start_shopping = 0;
if (user_name not in list_users_name) & (user_name not in list_forbid_user_name):
    print("检测到您是新用户，请先注册！\n")
    user_name = input("请输入注册的用户名：\n")
    while True:
        if (user_name in list_users_name):
            user_name = input("该用户名已注册，请重新申明用户名：\n")
        else:
            break
    user_key_1 = input("请设定登录密码：\n")
    user_key_2 = input("请再次确认密码：\n")
    while True:
        if (user_key_1 == user_key_2):
            print("注册成功！\n")
            break
        else:
            print("两次密码不一致，请重新设定登录密码：\n")
            user_key_1 = input("请设定登录密码：\n")
            user_key_2 = input("请再次确认密码：\n")

    user_wage = int(input("请输入您的工资：（元）\n"))
    new_user_info = '|'.join([user_name, user_key_1, str(user_wage)])
    f = open(r'E:/0have a try/python_learn/Day05/Users.txt','a',encoding='utf-8')
    f.write(new_user_info+'\n')  # 将新用户的信息按照格式追加写入Users.txt文件中
    start_shopping = 1  # 开始购物
elif (user_name in list_users_name) & (user_name not in list_forbid_user_name):
    user_key = list_users_key[list_users_name.index(user_name)]
    user_key_input = input("请输入用户密码（您有3次机会）：\n")
    for i in range(2):
        if user_key_input == user_key:
            print("登录成功！\n")
            user_wage = list_users_wage[list_users_name.index(user_name)]
            start_shopping = 1  # 开始购物
            break
        else:
            user_key_input = input("密码错误，请再次输入密码（您还有%d次机会）：\n"%(2-i))
    else:
        print("警告：您的密码累计输错3次，已将您的用户名添加进黑名单，并禁止该用户名登录！\n")
        forbid_user_name = list_users_name.pop(list_users_name.index(user_name))
        f = open('Blacklist.txt', 'a', encoding='utf-8')
        f.write(forbid_user_name + '\n')  # 将黑名单的用户名写入Blacklist.txt文件
        sys.exit()
else:
    print("警告：该用户名已被列进黑名单，请使用其他用户名登录！")
    sys.exit()

# 开始购物
count = [0,0,0]
print("恭喜您可以开始购物！有如下商品可以购买：\n")
print("1 iPhone\n2 mac bool\n3 bike")
while(user_wage>0):
    commodity = int(input("请输入想要购买商品的编号（输入-1可退出）：\n"))
    if commodity == 1:
        user_wage -= 1000
        count[0] += 1
    elif commodity == 2:
        user_wage -= 800
        count[1] += 1
    elif commodity == 3:
        user_wage -= 400
        count[2] += 1
    elif commodity == -1:
        print("您总共买了iPhone %d件，mac book %d件，bike %d件，还剩%d元\n"%(count[0],count[1],count[2],user_wage))
        sys.exit()
    else:
        print("您输入了非法字符，请重新输入。")
else:
    print("您的余额不足，您还差%d元，无法购买"%(-user_wage))
    sys.exit()