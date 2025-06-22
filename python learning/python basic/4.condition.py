flag = False
name = 'ldf'
if name == 'LDF':
    flag = True
    print('right')
else:
    print(name)

num = 5
if num == 3:  # 判断num的值
    print(3)
elif num == 2:
    print(2)
elif num == 1:
    print(1)
elif num < 0:  # 值小于零时输出
    print(0)
else:
    print(num)  # 条件均不成立时输出

fuck = 9
if fuck >= 0 and fuck <= 10:
    print('fuck')
else:
    print('bitch')

bitch=123
if bitch == 123 : print(bitch)

if not 1:
     print(1)
else:
    print(0)