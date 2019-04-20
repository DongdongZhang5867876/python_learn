#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 19:28
# @Author  : Zhnag Dongdong
# @File    : Test_try.py
# 按索引取值
hobbies = "music basketball"
print(hobbies[0])
print(hobbies[1])
print(hobbies[5])  # 因为5是空格，所以返回空格
print(hobbies[0:5])
print(hobbies[:5])
print(hobbies[0:5:2])
print(hobbies[0:5:-2])  # 我其实奇怪它为什么不报错
print(hobbies[11:5:-2])
print(hobbies[-1])  # 单独输入一个索引它就只会返回一个
print(hobbies[-3])
print(hobbies[1])

# 长度运算
print(len('name'))

# 成员运算
print('a' in 'Albert')
print('a' not in "Albert")

# 移除空白strip
print('    name'.lstrip())
print('name    '.rstrip())
print('    name    '.strip())

# 切分split，返回的是列表
print('n a me'.split(','))
print('n,a me'.split(','))
print('n,/a /me'.split('/',1))
print('n,/a /me'.split('/'))
print('a|b|c'.rsplit('|',1))  # 从右开始切割
print('n a me \n abc'.split(' '))  # split无视转义字符

# 组合join
print('a'.join('1234'))  # join其实是往字符里边间隔填充
print('a'.join('bcde'))
print(' '.join(['I','say','hello','world']))

# replace
print('abc name id'.replace('a','card'))  # 替换它会把每个'a'都替换
name = 'albert say :i have a dream,my name is albert'
print(name.replace('albert',"Albert",1))  # 只替换第一个
print(name)  # 注意此时name原来的值并没有改变，而是产生了一个替换之后新的值

# formate的三种用法
res = '{} {} {}'.format('Albert',18,'male')
print(res)
res = '{1} {0} {1}'.format('Albert',18,'male')
print(res)
res = '{name} {age} {sex}'.format(sex='male',name = 'Albert',age=18)
print(res)

# 字符串其他操作
# find,rfind,index,rindex,count
name = 'albert say hello'
print(name.find('o',1,3))  # 顾头不顾尾,找不到则返回-1不会报错,找到了则显示索引（那个1，3是查找范围）
# print(name.index('o',1,3))  # 同上,但是找不到会报错
print(name.count('e',1,3))  # 顾头不顾尾,如果不指定范围则查找所有
print(name.count('e'))

# center,ljust,rjust,zfill
name = 'albert'
print(name.center(30,'-'))  # 其实感觉也就第一个会用到
print(name.ljust(30,'*'))
print(name.rjust(30,'*'))
print(name.zfill(50))  # 用0填充

# expandtabs，控制空格大小，真感觉没什么用。。
name ='albe t\t H ello'
print(name)
print(name.expandtabs(1))
print(name.expandtabs(16))

# captalize,swapcase,title
print(name.capitalize())  # 首字母大写
print(name.swapcase())  # 大小写翻转
print(name.title())  # 每个单词的首字母大写

# is数字系列
num1 = b'4'  # bytes
num2 = u'4'  # unicode,python3中无需加u就是unicode
num3 = '四'  # 中文数字
num4 = 'IV'  # 罗马数字

# isdigt:bytes,unicode
print(num1.isdigit())
print(num2.isdigit())
print(num3.isdigit())
print(num4.isdigit())

'''
总结:
    最常用的是isdigit,可以判断bytes和unicode类型,这也是最常见的数字应用场景
    如果要判断中文数字或罗马数字,则需要用到isnumeric
'''
#is其他
print('===>')
name='alb123ert'
print(name.isalnum()) #字符串由字母或数字组成
print(name.isalpha()) #字符串只由字母组成

print(name.isidentifier())
print(name.islower())
print(name.isupper())
print(name.isspace())
print(name.istitle())