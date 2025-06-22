# 创建类
# class Employee:
#     '所有员工基类'
#     # 类变量，类所有实例之间共享 Employee.empCount
#     empCount = 0
#
#     # __init__，类的构造函数，初始化调用
#     # self，类的实例，self在定义类方法必须有，虽然在调用时不必传入相应参数
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)


# self代表类实例，而非类
# class Test:
#     # 类的方法，必须有第一个参数名称，默认self
#     def prt(self):
#         # self代表类实例，即当前对象地址
#         print(self)
#         # 指向类
#         print(self.__class__)
#
#
# t = Test()
#
# t.prt()


# 创建实例对象
# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# emp2.displayCount()

# 添加、删除、修改、类属性
# emp1.age = 7
# emp1.age = 8
# print(emp1.age)
# del emp1.age


# 内置属性
# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)


# 垃圾回收 ，引用计数
# a = 40      # 创建对象  <40>
# b = a       # 增加引用， <40> 的计数
# c = [b]     # 增加引用.  <40> 的计数
#
# del a       # 减少引用 <40> 的计数
# b = 100     # 减少引用 <40> 的计数
# c[0] = -1   # 减少引用 <40> 的计数


# 类继承
# class Parent:  # 定义父类
#     parentAttr = 100
#
#     def __init__(self):
#         print("调用父类构造函数")
#
#     def parentMethod(self):
#         print('调用父类方法')
#
#     def setAttr(self, attr):
#         Parent.parentAttr = attr
#
#     def getAttr(self):
#         print("父类属性 :", Parent.parentAttr)
#
#
# class Child(Parent):  # 定义子类
#     def __init__(self):
#         print("调用子类构造方法")
#
#     def childMethod(self):
#         print('调用子类方法')
#
#
# c = Child()  # 实例化子类
# c.childMethod()  # 调用子类的方法
# c.parentMethod()  # 调用父类方法
# c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
# c.getAttr()  # 再次调用父类的方法 - 获取属性值


# 方法重写
# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     # 子类重写方法
#     def myMethod(self):
#         print('调用子类方法')
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法

# 运算符重载
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)


# 类私有属性  两个下划线开头，是私有属性。__private_attrs
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名
# class Runoob:
#     __site = "www.runoob.com"
#
#
# runoob = Runoob()
# print(runoob._Runoob__site)


