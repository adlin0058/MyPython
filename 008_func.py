# # 函数调用
# # 绝对值abs
# # print(abs(100))

# # 最大值max
# # print(max(1, 2, 3))


# # 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
# # n1 = 255
# # n2 = 1000
# # print(hex(n1))
# # print(hex(n2))


# # 自定义函数

# # def my_abs(x):
# #     if x >= 0:
# #         return x
# #     else:
# #         return -x


# # print(my_abs(999))


# # # 占位符pass
# # def nop():
# #     pass


# # todo 计算平方根
# # import math


# # def quadratic(a, b, c):
# #     x1 = (-b+(math.sqrt((b**2)-4*a*c)))/(2*a)
# #     x2 = (-b-(math.sqrt((b**2)-4*a*c)))/(2*a)
# #     return x1, x2


# # print(quadratic(2, 3, 1))
# # print(quadratic(1, 3, -4))

# # todo 计算x的n次方
# # def power(x, n=2):
# #     s = 1
# #     while n > 0:
# #         n = n - 1
# #         s = s * x
# #     return s


# # print(power(3, 3))
# # print(power(5, 4))

# # todo 学生注册
# def enroll(name, gender, age=6, city='Shanghai'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#     print('---------------')


# enroll('Michael', 'M')
# enroll('Anay', 'F', city='America')

# #! 默认参数易错
# # def add_end(L=[]):
# #     L.append('END')
# #     return L


# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L


# print(add_end())
# print(add_end())

# #! 可变参数
# # todo 给定一组数字a，b，c……，请计算a^2 + b^2 + c^2 + ……


# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n**2
#     return sum


# print(calc())
# print(calc(1, 2, 3, 4))
# nums = [1, 2, 4, 5, 6]
# print(calc(*nums))


# #! 关键字参数 **kw
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)


# person('Michael', 21)
# person('Anay', 28, gender='F')
# person('Li', 33, gender='M', job='Engineer')
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Bob', 38, **extra)


# #! 命名关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)


# 匿名函数lambda
# def x(a): return a + 10


# print(x(5))

# def sum(arg1, arg2): return arg1 + arg2


# print('相加后的值为：', sum(10, 20))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
