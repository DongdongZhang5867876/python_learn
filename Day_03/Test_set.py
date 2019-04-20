#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 14:20
# @Author  : Zhnag Dongdong  
# @File    : Test_set.py
piano={'albert','孙悟空','周星驰','朱茵','林志玲'}
violin={'猪八戒','郭德纲','林忆莲','周星驰'}
# 求出既报名钢琴又报名小提琴课程的学员名字集合
print(piano & violin)
print(piano and violin)  # ？？？
# 求出所有报名的学生名字集合
print(piano | violin)
# 求出只报名钢琴课程的学员名字
print(piano - violin)
# 求出没有同时报这两门课程的学员名字集合
print(piano ^ violin)  # 重点！！！


