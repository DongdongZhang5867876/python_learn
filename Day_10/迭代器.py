#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 9:57
# @Author  : Zhnag Dongdong  
# @File    : 迭代器.py
dict1 = {'x':1,'y':2}
for i in dict1:  # 字典只能通过key值对
    n = 1
    while n < len(dict1):
        print(dict1[i])
        n += 1
dict1 = {'x':1,'y':2,'z':3}
iter_dict1 = dict1.__iter__()
print(iter_dict1.__next__())
print(iter_dict1.__next__())
print(iter_dict1.__next__())
print(dict1.__iter__().__next__())

set1 = {'a','b','c'}
iter_set1 = set1.__iter__()
print(iter_set1.__next__())
print(iter_set1.__next__())
print(iter_set1.__next__())

list1 = [1,2,3]
iter_list1 = list1.__iter__()
print(iter_list1.__next__())
print(iter_list1.__next__())
print(iter_list1.__iter__())

str1 = 'hello'
iter_str1 = str1.__iter__()
print(iter_str1.__next__())
print(iter_str1.__next__())
print(iter_str1.__iter__() is iter_str1)
print(iter_str1.__iter__().__iter__() is iter_str1)
print(iter_str1.__iter__().__iter__().__iter__().__iter__().__iter__() is iter_str1)

print('-'*40)
# 文件本身既是迭代器对象又是可迭代对象
f = open('a.txt','r',encoding = 'utf-8')
print(f.__iter__() is f)
print(f.__next__())  # 它不需要先.__iter__()就能.__next__()
print(f.__next__())


f = open('a.txt','r',encoding = 'utf-8')
while True:
    try:
        print(f.__next__())
    except StopIteration:
        break

set1 = {1,2,3,4,5,6}
iter_set1 = set1.__iter__()
while True:
    try:
        print(iter_set1.__next__())
    except StopIteration:
        break

dict1 = {'x': 1, 'y': 2, 'z': 3}
iter_dict1 = dict1.__iter__()
while True:
    try:
        print(iter_dict1.__next__())
    except StopIteration:
        break
# item = range(10000)
# iter_item = item.__iter__()
# while True:
#     try:
#         print(iter_item.__next__())
#     except StopIteration:
#         break
# for i in range(10000):
#     print(i)

x = [1, 2, 3]
iter_x = x.__iter__()
while True:
    try:
        print(iter_x.__next__())
    except StopIteration:
        break

print('第二次=================================>')

# iter_x = x.__iter__()  # 第二次要取的话还得重新重新定义iter_x
while True:
    try:
        print(iter_x.__next__())
    except StopIteration:
        break

x = [1,2,3]
iter_x = x.__iter__()
# print(len(iter_x))  # 没有获取长度的方法

file1 = open('a.txt','r',encoding='utf-8')
for line in file1:  # 它会自动 line = file1.__iter__().__next__()
    print(line)  #然后像上面print()打印出来

print('-'*40)
#yield
def test_yield():
    print('=========>first')
    yield 1
    print('=========>second')
    yield 2
    print('=========>third')
    yield 3

print(test_yield())  # 生成器无法通过函数调用的方式使用，print()只能打印出它的生成地址
res = test_yield()
print(res.__iter__() is res)
print(res.__next__())
print(res.__next__())
print(res.__next__())

print('-'*50)
def my_range(start,stop,step=1):  # 默认参数必须写在最后面
    n = start
    while n < stop:
        yield n  # yield可多次返回
        n += step

for i in my_range(3,10,3):
    print(i)

def eat(name):
    print('(1) %s is ready for eating'%name)
    while True:
        food = yield  # yield可以赋值给一个变量
        print('(2) %s starts to eat %s'%(name,food))

person1 =eat('Albert')
person1.__next__()
person1.__next__()

"""
对于表达式形式的yield，在使用前必先初始化
即第一次必须传None，或者用__next__方法
"""
# person1.send(None)  # 初始化，和下面一行代码同等效果
person1.__next__()
person1.send('烤鸭')  # send有两个功能：1 传值，2 初始化
person1.send('熊掌')
person1.send('大象')
person1.close()


print('-'*50)
def eat(name):
    print('%s is ready for eating' % name)
    food_list = []
    while True:
        food = yield food_list
        print('%s starts to eat %s' % (name, food))
        food_list.append(food)
name = 'Albert'
person1 = eat(name)
person1.send(None)
# person1.__next__()

res1 = person1.send('蒸羊羔')
print('%s has eaten %s' % (name, res1))
res2 = person1.send('蒸鹿茸')
print('%s has eaten %s' % (name, res2))
res3 = person1.send('蒸熊掌')
print('%s has eaten %s' % (name, res3))
res4 = person1.send('烧素鸭')
print('%s has eaten %s' % (name, res4))
person1.close()  # 关闭之后，后面的就吃不了了，也不能兜着走


print('-'*50)
def eat(name):
    print('%s is ready for eating' % name)
    food_list = []
    while True:
        food = yield food_list
        print('%s starts to eat %s' % (name, food))
        food_list.append(food)
        print('%s has eaten %s' % (name, food_list))
person1 = eat('Albert')
person1.send(None)
person1.send('蒸羊羔')
person1.send('蒸鹿茸')
person1.send('蒸熊掌')
person1.send('烧素鸭')
person1.close()