#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 10:56
# @Author  : Zhnag Dongdong  
# @File    : Test_List.py
# 给列表添加元素
# append方法 在列表最后追加元素
li = ['a','b','c','d']
li.append('e')
print(li)
print(li.append('f'))  # .append()本身只起队尾追加的作用，没有返回值
print(li)

# 插入
li.insert(3,'x')  # 从开头数0，从间隔数1
print(li)

# extend可以追加多个元素
li = [1,2,3,4,5]
li.append([6,7,8,9,10])  # append会把[6,7,8,9,10]作为一个元素追加输入
print(li)
li = [1,2,3,4,5]
li.extend([6,7,8,9])  # extend会把[6,7,8,9,10]打散追加输入
print(li)
li.extend('abc')  # 'abc'是作为3个元素输入的
print(li)
li.extend('a')
print(li)
#li.extend(1)  # extend在执行添加的时候，被传入的参数必须是可迭代对象
print(li)

# 删除列表的元素
# pop弹出删除 有返回值（因为是弹出啊），默认弹出列表中最后一个，指定删除索引值
li = [1,2,3,4,5,6]
print(li.pop())  # 这是有返回值的
print(li)
print(li.pop(3))  # 指定列表中的索引值
print(li)

print('我是分隔符'.center(30,'-'))

# remove 删除 没有返回值，没有默认值，需要指定被删除的元素（只能直接指定元素不能指定索引值）
li = [1,2,3,4,5,6,'我']
print(li.remove(4))  # 注意这个4 是真的2，不是索引值，它没有返回值
print(li)
li.remove('我')
print(li)
# print(li.remove())  # 必须给它指定删除什么，不能不指定

# clear 删除 保留列表名称，清空里面的值
li = ['a', 'b', 'c', 'd', 'e', 'b', 'c']
li.clear()
print(li)

# del 删除 通用删除 但是一般不用
li = ['a', 'b', 'c', 'd', 'e', 'b', 'c']
del li[2]  # 按索引删除（这个和remove('c')按元素删除的区别）
print(li)
li = ['a', 'b', 'c', 'd', 'e', 'b', 'c']
del li  # 在内存中删除l1 相当于没有定义l1
# print(li) #报错

# 更改列表中元素
li = [1, 2, 3, ]
li[2] = 4  # 当然是按索引替换的拉
print(li)

print('我是分隔符'.center(30,'-'))

# 查找列表中的元素
# 按照索引或者指定列表中的元素查找
li = ['a', 'b', 'c', 'd', 'e', 'b', 'c']
print(li.index('a'))  # 返回索引值（只返回找到的第一个的索引值）
print(li.index('b',1,4))  # 两个数字分别对应起始位置和结束位置
print(li[0:5]) # 按照索引取值和字符串的用法相同
print(li[:5])
print(li[0:5:2])
print(li[:-1])
print(li[:-2])
print(li[5:1:-2])

# 使用enumerate对列表枚举
li = ['a', 'b', 'c', 'd', 'e','a']
for i,x in enumerate(li,1):
    print(i,x)

print(len(li))  # 统计列表长度

print(li.count('a'))  # 统计列表中元素的次数

# 给列表排序
# reverse 反序排序
li = ['a',1,'b','c','d','e','a','b','c']
li.reverse()  # reverse()会直接作用于原列表
print(li)

# sort 按照ascii码来进行排序
li = ['a', '1', 'b', 'c', 'd', 'e', 'b', 'A', 'Z', 'c']
li.sort()  # sort()会直接作用于原列表
print(li)
li.sort(reverse=True)  # sort(reverse=True)进行反向排序
print(li)

