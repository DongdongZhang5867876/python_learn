#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 9:07
# @Author  : Zhnag Dongdong  
# @File    : spam.py.py
# 修改后的spam模块
# 规定*的调用只调用money和read1这两个功能
__all__ = ['money','read1']

print('from the spam.py')
money = 1000  # 这个定义的是模块的属性
def read1():  # 这个定义模型的方法（函数即方法）
    print('spam模块.read1:',money)

def read2():  # 有函数嵌套
    print('spam模块.read2')
    read1()

def change():
    global money  # 模块中变量和函数以模块所在的名称空间当做全局名称空间
    money = 1

print(__name__)
# __name__的值
# 1 在文件被直接执行的情况下，等于'__main__'
# 2 在文件被导入的情况下，等于模块名
if __name__ == '__main__':  # __main__就是标志我这个文件是否是被执行的主文件
    print('【脚本执行成功】')  # 文件被当作脚本执行
    print('这是我不希望在模块导入时被执行的部分！！')
    read1()  # 文件被模块导入时不希望被执行的部分
else:
    print('【模块导入成功】')  # 文件被当作模块导入
