# number可以当键
d = {123: 1}
print(d[123])

# string可以当键
d['123'] = 2
print(d['123'])

# 元组可以当键
d[(1, 2, 3)] = 4
print(d)

del d[(1, 2, 3)]
print(d)

d.clear()
print(d)
del d

person = {'name': "ldf", 'age': '24'}
print(len(person),type(person))
