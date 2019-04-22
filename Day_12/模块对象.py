#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 23:58
# @Author  : Zhnag Dongdong  
# @File    : 模块对象.py
# Python文件
import  spam
print(spam)
money = 588
print(money)
print(spam.money)  # 模块中的（全局）变量不会与使用者自己定义的变量冲突（因为所在的名称空间不一样）
spam.read1()
spam.read2()

print('{:~^50}'.format("我是一条神奇的分隔线"))
spam.change()
print(spam.money)
spam.read1()
money = 10
read1 = 2
read2 = 3
print(spam.read1)
print(spam.read1())
spam.read1()
spam.read2()
spam.change()
print(money)
spam.read1()  # 同理，使用者申明的同名变量的改变不会影响到模块中的变量

spam.money = 200  # 但是直接对模块中变量的改变当然会影响到所导入的模块中的变量的值（只会影响到所导入的模块中的变量值）
print(spam.money)
spam.read1()

print('{:~^50}'.format("我是一条神奇的分隔线"))
import spam as sm  # 为模块起别名
print(sm.money)
sm.read1()
sm.read2()

print('{:~^50}'.format("我是一条神奇的分隔线"))
from spam import money as mo
from spam import read1, read2, change
print(mo)
read1()
read2()
change()
print(money)

del mo,money,read1,read2,change
print('{:~^50}'.format("我是一条神奇的分隔线"))
from spam import money as mo  # 模块中的变量或函数也都可以起别名
from spam import money, read1, read2, change
print(mo)
read1()
read2()
change()
print(mo)
mo = 3  # 对从模块中导入变量的修改不会影响到模块本身的变量
money = 3
read1()  # 输出还是1000
read1 = 3  # 但对函数的修改会影响到导入的函数
# read1()  # 无法调用

print('{:~^50}'.format("我是一条神奇的分隔线"))
del read1,read2,money,mo
from spam import *
print(money)
read1()
money = 3
print(money)
read1()  # 即使导入*也还是无法改变模块中方法与模块中变量的关系
# read2()  # 设置*之后无法调用

print('{:~^50}'.format("我是一条神奇的分隔线"))

# 1 验证先查找内存中加载的模块
import time
import spam
print(spam.money)

time.sleep(5)
import spam
print(spam.money)

# 2 验证内置模块的查找==》在sys.path下已经自定义了一个time.py文件，然而仍然没有导入，说明内置模块是优先于自定义模块导入的
import sys
import time
print(time)
print('time' in sys.modules)  # sys.modules存放着内存中被导入的模块
import time  # 内置模块默认在硬盘，导入之后才会进入内存
time.sleep(3)
print('time' in sys.modules)

# 3 sys.path路径包含的模块(重点)
import sys
print(sys.path)
sys.path.append(r'E:/0have a try/python_learn/Day_12/X')  # 把x文件夹路径加入到sys.path路径下
print(sys.path)

print('{:~^50}'.format('我是一条神奇的波浪线'))
# import a.x1,a.y1
'''
1 产生一个包的名称空间
2 执行包下的__init__.py文件，将产生的名字存放于包的名称空间中
3 在当前执行文件中拿到一个名字a，该名字指向包的名称空间
'''
# a.x1.func1()  # 通过"文件名.py名.函数名"的形式调用
# a.y1.func2()
# print(a.x1.func1)

# from a.x1 import func1
# from X.a import x1
# x1.func1()

from X.a.x1 import func1
func1()

from X.a import y1
y1.func2()

import time
print(time.time())
start_time = time.time()
time.sleep(1)
stop_time = time.time()
print(stop_time-start_time)

print(time.strftime("%y-%m-%d"))
print(time.strftime('%y-%m-%d %H:%M:%S %p'))  # 时分秒必须大写用:
print(time.strftime("%Y_%M:%D %H:%M:%S %p"))  # 可以用 _ : 混合连接

print(time.localtime())
print(time.localtime().tm_mday)

print(time.gmtime())  # 本初子午线时间

import re
print(re.findall('\w', 'ab 12\+- *&_'))  # 匹配字母数字和下划线
print(re.findall('\W', 'ab 12\+- *&_'))  # 匹配非字母数字下划线
print(re.findall('\s', 'ab \r1\n2\t\+- *&_'))  # 匹配任意空白字符
print(re.findall('\S', 'ab \r1\n2\t\+- *&_'))  # 匹配任意非空字符
print(re.findall('\d', 'ab \r1\n2\t\+- *&_'))  # 匹配任意数字
print(re.findall('\D', 'ab \r1\n2\t\+- *&_'))  # 匹配任意非数字
print(re.findall('\w_nb', 'albert james_nb123123curry_nb,harden_nb'))