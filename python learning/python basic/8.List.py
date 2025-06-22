list1 = ['a', 'b', 'c']
print(list1[0], list1[1:], list1[1:2])

# 列表的增
list1.append('d')
list1.append('e')
print('增', list1)

# 列表的删
del list1[1]
print('删', list1)
print(['fuck'] * 4, len(['fuck']))
print([123] + [456])
print(3 in [1, 2, 3])
for x in [1, 2, 3]: print(x)

mother = [1, 2, 3]
fuck = [4, 5, 6]
mother.extend(fuck)
print(mother)