#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 23:26
# @Author  : Zhnag Dongdong  
# @File    : 文件处理.py
# 打开文件
f = open(r'E:\0have a try\python_learn\Day04\a.txt',mode='r',encoding='utf-8')
# 读取文件
data = f.read()
# print(data)
f.close()
print(f)
# f.read()  # 文件关闭不能再进行读取

with open(r'E:\0have a try\python_learn\Day04\a.txt','r',encoding = 'utf-8') as f:
    data = f.read()
    print(data)

with open(r"E:\0have a try\python_learn\Day04\a1.txt",'r',encoding = 'utf-8') as f1,\
    open('a2.txt','r',encoding = 'utf-8') as f2:
    data1 = f1.read()
    data2 = f2.read()

# 操作文件”r"模式
# 全部读取使用read
f = open('a.txt', mode='r', encoding='utf-8')  # “r”模式下，如果文件不存在会报错
# f.write('哈哈') #抛出异常，不能写
print(f.readable())  # 判断是否可读
print('=============>1')
print(f.read())  # 全部读取
print('=============>2')
# 读文件会有一个光标移动，第一次读完了，光标移至末尾，第二次读无内容
print(f.read())
f.close()

# 一行一行读文件内容使用readline
f = open('a.txt', mode='r', encoding='utf-8')
# readline指的是一行一行读文件
print(f.readline(), end='')  # 文件中有换行，print也自带换行，指定end参数去掉默认换行
print(f.readline(), end='')
print(f.readline(), end='')
f.close()

# 全部读取文件内容，存入列表，每行内容为列表的一个元素使用readlines
f = open('a.txt', mode='r', encoding='utf-8')

print(f.readlines())
f.close()