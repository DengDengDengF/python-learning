# 算数运算符
a = 10
b = 20
# a的b次方
print(a ** b)
# 整除，向下取整
print(9 // 2)

# 比较运算符  ==运算符比较值
if a <= b:
    print('true')
else:
    print('false')

# 赋值运算符
c = 1
c //= a
print(c)

# 位运算
'''
& 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 
| 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
^ 按位异或运算符：当两对应的二进位相异时，结果为1
~ 按位取反运算符：将二进制表示中的每一位取反，0 变为 1，1 变为 0。
<< 左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。相当于,原来数字 * (2 ** n)
>> 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数。相当于，原来的数字 / (2 ** n)
'''

# 成员运算符 in    not in

ArrList = [1, 2, 3, 4, 5]
if (a in ArrList):
    print('true')
else:
    print('false')

if (a not in ArrList):
    print('true')
else:
    print('false')

# 身份运算符 is is not  比较地址
if (a is b):
    print('true')
else:
    print('false')

a = 20
if (a is not b):
    print('false')
else:
    print('true')

a = [2, 1, 3]
b = a[:]
print(b is a)
print(b == a)
# 运算符优先级
