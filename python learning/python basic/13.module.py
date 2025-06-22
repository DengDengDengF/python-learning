import math


Money = 2000
def AddMoney():
    # python会首先猜测他是个局部变量，如果不声明他是个全局变量，它会报错
    global Money
    Money = Money + 1
    return


print(Money)
AddMoney()
print(Money)

print(dir(math))