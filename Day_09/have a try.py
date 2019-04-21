def eat(name):
    print('【1】%s is ready for eating' % name)
    while True:
        food = yield  # 这是yield表达式形式，yield可以赋值给一个变量
        print('【2】%s starts to eat %s' % (name, food))


person1 = eat('Albert')

# 函数暂停在food = yield这行代码
person1.__next__()

# 继续执行代码，由于yield没有值，即yield = None，则food = None
person1.__next__()