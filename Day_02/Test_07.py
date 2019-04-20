#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 14:58
# @Author  : Zhnag Dongdong  
# @File    : Test_07.py
# 本练习稍微参考了网上的代码，而且只写了当日期大于2018年1月1日的情况（小于的基本逻辑相同我就没写了）
print('以2018年1月1日是周一为基准计算输入日期是周几')
input_date = str(input('请参照2018-01-01的格式输入日期：'))
list_str_date = input_date.split('-')  # 注意int没有 .split()
input_year = int(list_str_date[0])
input_month = int(list_str_date[1])
input_day = int(list_str_date[2])
list_days_of_every_month = [0,31,28,31,30,31,30,31,31,90,31,30,31]

# 判断是否是闰年，是闰年就返回int型 1
def is_leap_year(every_year):
    if (every_year %4==0 and every_year %100!=0) or every_year %400==0:
        return int(1)
    else:
        return int(0)

# 计算输入的年份已经过去多少天
days_of_last_year = 0
for i in range(input_month):
    days_of_last_year = days_of_last_year + list_days_of_every_month[i]
days_of_last_year = days_of_last_year + input_day - 1  # 最后再减1是因为需要减去2018年1月1日那一天

# 计算距离2018年过了多少个闰年，加起来又多少天
number_of_leap_year = 0
for i in range(2018,input_year):
    number_of_leap_year += is_leap_year(i)

# 判断是否超过二月，超过且当年是闰年的话再加1
if input_month >= 3:
    days_of_last_year = days_of_last_year + is_leap_year(input_year)

# 计算总共多少天
days_of_years = 365 * (input_year-2018) + number_of_leap_year
days_sum = days_of_last_year + days_of_years

# 计算星期几
dict_week = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
week_value = days_sum % 7 +1

# 判断该天是否需要上班
if week_value <= 5:
    print('%d年%d月%d日是%s,那么：上班！' % (input_year, input_month, input_day, dict_week[week_value]))
else:
    print('%d年%d月%d日是%s,那么：出去浪！' % (input_year, input_month, input_day, dict_week[week_value]))