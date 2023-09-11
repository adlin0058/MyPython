# class MyClass:
#     i = 12345

#     def f(self):
#         return 'hello world'


# # 类实例化
# x = MyClass()

# # 访问类的属性和方法
# print('MyClass类的属性i为：', x.i)
# print('MyClass类的方法f输出为：', x.f())


# # 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性，类外部无法访问
#     __weight = 0
#     # 定义构造方法

#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w

#     def speak(self):
#         print('%s 说：我%d岁。' % (self.name, self.age))


# # 实例化类
# # p = people('runoob', 10, 30)
# # p.speak()

# #! 继承
# class student(people):
#     grade = ''

#     def __init__(self, n, a, w, g):
#         # 调用父类的构造函数
#         people.__init__(self, n, a, w)
#         self.grade = g
#     # 覆写父类的方法

#     def speak(self):
#         print('%s说：我%d岁了，在读%d年级' % (self.name, self.age, self.grade))

# # 另一个类，多继承前的准备


# class speaker():
#     topic = ''
#     name = ''

#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t

#     def speak(self):
#         print('我叫%s，是一个演讲家，我演讲的主题是%s' % (self.name, self.topic))


# #! 多继承
# class sample(speaker, student):
#     a = ''

#     def __init__(self, n, a, w, g, t):
#         student.__init__(self, n, a, w, g)
#         speaker.__init__(self, n, t)


# test = sample('Tim', 25, 80, 4, 'Python')
# test.speak()


# #! 方法重写
# class Parent:
#     def myMethod(self):
#         print('调用父类方法')


# class Child():
#     def myMethod(self):
#         print('调用子类方法')


# c = Child()
# c.myMethod()
# # * 用子类调用父类的一个方法
# super(Child, c).myMethod()


# #! 类属性与方法

# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量

#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)


# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# # print(counter.__secretCount)  # 报错


# #! 私有方法实例
# class Site:
#     def __init__(self, name, url):
#         self.name = name
#         self.__url = url  # private

#     def who(self):
#         print('name :', self.name)
#         print('url  :', self.__url)

#     def __foo(self):
#         print('这是私有方法')

#     def foo(self):
#         print('这是公有方法')


# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()
# x.foo()
# x.__foo()  # 错误


# #! 运算符重载
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)

#     def __add__(self, other):
#         return Vector(self.a+other.a, self.b+other.b)


# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1+v2)
