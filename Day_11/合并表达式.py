#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 16:06
# @Author  : Zhnag Dongdong  
# @File    : 合并表达式.py
x = 1
y = 2
print(x if x<y else y)
def max2(x,y):
    return x if x>y else y
print(max2(10,11))

# def foo():
#     print('from foo')
#     foo()
# foo()

def get_age(n):
    if n == 1:
        return 18
    else:
        return get_age(n-1) + 2
print(get_age(4))

list1=[1,[2,[3,[4,[5,[6,[7,[8,[9,[10,]]]]]]]]]]

def tell(li):
    for item in li:  # 每次递归都一定要有一个剥离的过程！！！
        if type(item) is not list:
            print(item)
        else:
            tell(item)

tell(list1)

add = lambda *args : sum(args)
print(add(5,46))
print(max([3,2,5,44,66,11,13]))
print(min([3,2,5,44,66,11,13]))
print(sorted([3,2,5,44,66,11,13]))
print(sorted([3,2,5,44,66,11,13],reverse=True))

salaries = {
    'james': 300000,
    'kd': 100000,
    'zimuge': 10000,
    'harden': 90000
}
print(max(salaries))
print(min(salaries))
print(sorted(salaries))  # max,min,sorted是基于for循环，列表默认比较的是key值，显然不对

print(max(salaries,key=lambda x:salaries[x]))
print(min(salaries,key = lambda x:salaries[x]))
print(sorted(salaries,key=lambda x:salaries[x]))
print(sorted(salaries,key=lambda x:salaries[x],reverse=True))

def format_name(s):
    s1 = s[0:1].upper()+s[1:].lower()
    return s1
new_list = list(map(format_name,['adam', 'LISA', 'barT']))
print(new_list)

nums = [1,2,3,4,5,6]
res = list(map(lambda x:x**2,nums))
print(res)

iter_res = map(lambda x:x**2,nums)
print(iter_res.__iter__() is iter_res)
print(iter_res.__next__())
while True:
    try:
        print(iter_res.__next__())
    except StopIteration:
        break

names = ['JAMEs', 'HaRDEn', 'CuRRy']
res = map(lambda x:x[0:1].upper() + x[1:].lower(),names)
print(list(res))

names = ['James', 'Harden', 'Curry']
res = map(lambda x:x+'is a super star\n',names)
print(*list(res))

from functools import reduce
# 计算1+2+3+++++100
res = reduce(lambda x,y:x+y, range(1,101),0)
print(res)
res = reduce(lambda x,y:x+y, range(1,101))
print(res)

list1 = ['Today', 'is', 'the', 'first', 'day', 'of', 'the', 'rest', 'of', 'your', 'life']
res = reduce(lambda x,y:x+' '+y+' ',list1)
print(res)

# 过滤出年龄不小于30的
ages = [18, 19, 10, 23, 99, 30]
res = filter(lambda x: x>=30, ages)  # filter(判断句，列表) 只能过滤真假，返回判断句是真的列表
print(list(res))  # filter同map一样，返回的值是个迭代器，需要list()才能直接打印，或者用迭代的方式打印

# 过滤出裁判
names = ['James is super star', 'Harden is super star', 'Albert is referee']
res = filter(lambda x:x.endswith('referee'),names)
print(list(res))

res = '{2} {1} {0}'.format('Albert',16,'male')
print(res)

C = (250,250)
print('敌人坐标：{}'.format(C))

print('{:-<10}'.format('18'))
print('{:*^50}'.format("我是一条快乐的分界线"))
print('{:~<50}'.format("我是一条快乐的波浪线"))
print('a'.zfill(10))

# 精度通常和float类型一起使用
# 其中.5表示长度为5的精度
# 3.14159
print('{:.5f}'.format(3.14159265753))

print('{:,}'.format(123456789))

print('{:b}'.format(20))
print('{:d}'.format(20))
print('{:o}'.format(20))
print('{:x}'.format(20))

print(abs(-561))

print(all([1,'sadf',5,True]))  # 列表中所有元素的布尔值为真，最终结果才为真
print(any([0,'dgeg',None,False]))  # 列表中所有元素的布尔值只要有一个为真，最终结果就为真
print(any([]))  # 传给any的可迭代对象如果为空，最终结果为假

print(bool('sdf'))  # bool值判断，0,None,空的布尔值为假

print(bin(11))  # 十进制转二进制
print(oct(11))  # 十进制转八进制
print(hex(11))  # 十进制转十六进制

res = bytes('你好Albert',encoding='utf-8')
print(res)


def func():
    pass

print(callable(func))
print(callable('abc'.strip))  # .strip可以调用，因为可以加()
print(callable(max))

print(chr(90))
print(ord('Z'))

# 查看对象下可调用的方法
print(dir('abc'))  # 查看某个对象下可以调用到哪些方法

print(divmod(1311,25))

# 将字符内的表达式拿出运行一下，并拿到该表达式的执行结果===》变字符串为可运行内容
res1 = eval('2*3')
print(res1, type(res1))
res2 = eval('[1,2,3,4]')
print(res2,type(res2))
res3 = eval('{"name":"Albert","age":18}')
print(res3,type(res3))

s = {1,2,3}
s.add(4)
print(s)

f_set = frozenset({1,2,3})  # 不可变集合
# f_set.add(5)  # 说了不可变就当然没法给它添加元素了！！
print(f_set)

print(globals())  # 查看全局作用域中的名字与值的绑定关系
print(dir(globals()['__builtins__']))

def func():
    x = 1
    print(locals())  # 查看局部作用域中的名字与值的绑定关系

func()

print(hash('a'))
print(hash((1,2,3,4)))
# 不可hash的类型list,dict,set==  可变的类型
# 可hash的类型int,float,str,tuple ==  不可变的类型
# dict1 = {[1, 2, 3]: 'a'}  # 报错，字典的key必须是不可变类型

def func():
    """
    帮助信息
    :return: None
    """
    pass
print(help(func))

print('{:~^50}'.format('我是一条很浪的分隔线'))
print(len({'x':1,'y':2}))  # 触发 {'x':1,'y':2}.__len__()
print({'x':1,'y':2}.__len__())  # 与上面等同
obj = iter('Albert')  # 等价于'Albert'.__iter__()
print(next(obj))  # 等价于obj.__next__()

print(pow(2,3,3))
print(2**3%3)

li = [1,4,3,5,0]
print(li)
print(list(reversed(li)))

print(round(4.5))  # 它的.5不入
print(round(4.3))
print(round(4.6))

# 切片对象
sc = slice(1, 5, 2)  # 1:5:2
l = ['a', 'b', 'c', 'd', 'e', 'f']
# print(l[1:5:2])
print(l[sc])

t = (1, 2, 3, 4, 5, 6, 7, 8)
# print(t[1:5:2])
print(t[sc])

# 求和
print(sum([1, 2, 3, 4]))

# 拉链函数
left = 'hello'
right1 = {'x': 1, 'y': 2, 'z': 3}
right2 = [1, 2, 3, 4, 5]

res1 = zip(left, right1)
res2 = zip(left, right2)
print(list(res1))
print(list(res2))

import time
time1 = time.time()
l1 = ['egg%s'%i for i in range(1000000)]
time2 = time.time()
print(time2-time1)

time3 = time.time()
li = []
for i in range(1000000):
    li.append('egg%s'%i)
time4 = time.time()
print(time4-time3)

li = ('egg%s'% i for i  in range(1000000) if i > 100000)
print(next(li))
print(next(li))