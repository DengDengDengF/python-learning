#!/usr/bin/python
# -*- coding: UTF-8 -*-
#  本文探讨变量

# number
# 整型 浮点 字符串
age = 100
weight = 100.0
# string
name = 'ldf'

print(age, weight, name)

# 多变量赋值
a = b = c = 1
print(a, b, c)
# 多变量对象赋值
a, b, c = 1, 2, 3
print(a, b, c)

# 字符串截取[头下标:尾下标],从头下标截取，但是不包含尾下标的字符
s = 'abcdef'
print(s[1:5])

str = "hello world"
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
# *就是重复操作
print(str * 2)
# +就是连接运算符
print(str + "fuck")

letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o'];
# 第三个参数是步长，间隔截取
print(letters[1:7:2])

# 列表list
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

# 列表 list 允许更新
# list[0] = 123

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

# 元组 相当于只读列表
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

# 元组 tuple 不允许更新
# tuple[0] = 123

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

# 字典 dict  string number可以当key 变量也可以当key
dict = {}
dict['name'] = 'ldf'
dict['ages'] = 24
print(dict)
print(dict['name'],dict['ages'])
print('---')
print(dict.keys())
print(dict.values())

