# class MyClass:
#     i = 12345

#     def f(self):
#         return 'hello world'


# # 类实例化
# x = MyClass()

# # 访问类的属性和方法
# print('MyClass类的属性i为：', x.i)
# print('MyClass类的方法f输出为：', x.f())


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，类外部无法访问
    __weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s 说：我%d岁。' % (self.name, self.age))


# 实例化类
# p = people('runoob', 10, 30)
# p.speak()

#! 继承
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法

    def speak(self):
        print('%s说：我%d岁了，在读%d年级' % (self.name, self.age, self.grade))

# 另一个类，多继承前的准备


class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print('我叫%s，是一个演讲家，我演讲的主题是%s' % (self.name, self.topic))


# 多继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample('Tim', 25, 80, 4, 'Python')
test.speak()
