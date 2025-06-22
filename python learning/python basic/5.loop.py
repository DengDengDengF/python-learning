a = 1
while a < 10:
    a += 2
    print(a)
else:
    print(a)

a = [1, 2, 3]
b = a[:]
while a is b:
    print('no fucking way')
else:
    print('yes')

name = 'ldf'
for letter in 'ldf':
    print(letter)

fruits = ['banana', 'orange', 'fuck']
for fruit in fruits:
    print(fruit)

state = 1
for index in range(0, len(fruits), state):

    print(fruits[index])
else:
    print(index)


for index in  'ldf':
    print(index)
else:
    print(index)
