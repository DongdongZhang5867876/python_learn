#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 14:20
# @Author  : Zhnag Dongdong  
# @File    : Test_dict.py
# 给字典增加元素
# 通过键值对的方式
li = {'name':'albert','age':18,'gender':'male'}
print(li)
li['hobbies'] = 'music'  # 字典可以通过方括号[]添加元素！！
print(li)

# 删除字典中的元素
# del 通过字典的key删除
li = {'name':'albert','age':18,'gender':'male'}
del li['name']
print(li)
print('我是一条分隔线'.center(30,'-'))

# pop 弹出删除
li = {'name':'albert','age':18,'gender':'male'}
li_pop = li.pop('name')  # 返回弹出的值
print(li_pop)
print(li)
print(li.popitem())
# print(li.pop())  # 不能直接使用pop()，只能用popitem()，很奇怪

# 更改字典中的元素
# 通过键值对的方式
li = {'name':'albert','age':18,'gender':'male'}
li['name'] = '张冬冬'
print(li)

# 通过update 更新（写法和定义字典一样）
li = {'name':'albert','age':18,'gender':'male'}
li.update({'name':"张冬冬",'hobby':'swimming'})
print(li)

print('我是一条分隔线'.center(30,'-'))
# 查找字典中的元素
# 通过键值对查找
li = {'name':'albert','age':18,'gender':'male'}
print(li['name'])  # 通过键值对找不到它会报错！！
# 通过get方法查找
print(li.get('hobby'))  # 通过get对找不到它不会报错！！

li = {'name': 'albert', 'age': 18, 'gender': 'male','3':3,}
# 通过enumerate 枚举
for a in enumerate(li):
    print(a)

# .keys(),.values(),.items()
print(li.keys())
print(li.values())
print(li.items())  # 打印全部

# 通过for循环遍历
for k,v in li.items():
    print(k,v)








