# 函数调用
# 绝对值abs
# print(abs(100))

# 最大值max
# print(max(1, 2, 3))


# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))


# 自定义函数

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x


# print(my_abs(999))


# # 占位符pass
# def nop():
#     pass


# todo 计算平方根
# import math


# def quadratic(a, b, c):
#     x1 = (-b+(math.sqrt((b**2)-4*a*c)))/(2*a)
#     x2 = (-b-(math.sqrt((b**2)-4*a*c)))/(2*a)
#     return x1, x2


# print(quadratic(2, 3, 1))
# print(quadratic(1, 3, -4))

# todo 计算x的n次方
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 3))
print(power(5, 4))
