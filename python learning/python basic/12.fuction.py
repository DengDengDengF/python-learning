# def 定义函数
def printme(str):
    # 打印字符串
    print(str)
    return


printme('fuck')


# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 以下测试 可变对象与不可变对象

def test(num, obj):
    num = 2
    obj['key'] = 2
    print('test函数块内部修改后', num, obj)
    return


num = 1
obj = {'key': 1}
test(num, obj)
print('test函数块外部修改后', num, obj)


# 不定长输出
def printList(str, *list):
    print(str)
    for item in list:
        print(item)
        print()
    return


str = '123'
printList(str)
printList('str', 1, 2, 3)

# 匿名函数 lambda
sum = lambda arg1, arg2: arg1 + arg2
print('相加后的值', sum(1, 2))
print('相加后的值', sum(10, 20))


# return

def add(arg1, arg2):
    sums = arg1 + arg2
    return sums


print('add()', add(100, 200))
# print(sums) sums在add()局部作用域

