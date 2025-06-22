tup1 = ('l', 'd', 'f')
print(tup1[0], tup1[1:2])
# 要加入逗号不然 元组相加报错
tup2 = ('50',)
print(tup2)

# 不允许修改但是可以连接
tup3 = tup1 + tup2
print(tup3)

# 不允许删除但是可以删除整个元组
tup4 = ('fuck', 'you')
print(tup4)
del tup4
# print(tup4) 删除后打印出异常信息

# 任意无符号的对象，以逗号隔开，默认为元组
print('abc', -4.24e93, 18 + 6.6j, 'xyz')
x, y = 1, 2
print("Value of x , y : ", x, y)


