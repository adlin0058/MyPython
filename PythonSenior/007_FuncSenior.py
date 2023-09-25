
# #! 高阶函数map

# def f(x):
#     return x*x


# #       函数  迭代器
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# # map 返回的也是一个迭代器
# print(list(r))


# r2 = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(r2)


from functools import reduce


# #todo 求[1,3,5,7,9]的和
# def add(x, y):
#     return x+y


# r1 = reduce(add, [1, 3, 5, 7, 9])
# print(r1)


# # todo 将[1,3,5,7,9]变换成整数13579
# def fn(x, y):
#     return x*10+y


# r2 = reduce(fn, [1, 3, 5, 7, 9])
# print(r2)

# # todo 将字符串'13579'转换成int
# def fn(x, y):
#     return x*10+y

# # todo 将 数字字符 转换为 数字


# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]


# r3 = reduce(fn, map(char2num, '13579'))
# print(r3)

# todo 利用lambda函数简化

# digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#           '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# def char2num(s):
#     return digits[s]


# def str2int(s):
#     return reduce(lambda x, y: x*10+y, map(char2num, s))


# r4 = str2int('2468')
# print(r4)


# # todo 将字符串变为英文名字格式
# def normalize(name):
#     return name.title()


# r1 = map(normalize, ['adam', 'LISA', 'barT'])
# print(list(r1))


# todo 利用map和reduce，将字符串'123.456'转换为浮点数123.456


def str2float(s):
    s_int = s.split('.')[0]
    s_float = '0.'+s.split('.')[1]
    r = reduce(lambda x, y: x+y, map(float, [s_int, s_float]))
    return r


r = str2float('123.456')
print(r)
