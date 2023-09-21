# 递归函数

# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return n*fact(n-1)


# print(fact(0))
# print(fact(1))

# print(fact(6))

# # 函数调用是通过栈实现的
# # 栈大小有限
# #! fact(1000)时会导致栈溢出

# # ? 尾递归优化 可解决栈溢出的问题
# # ? 尾递归是指，在函数返回的时候，
# # ? 调用自身本身，并且，return语句不能包含表达式

# def fact(n):
#     if n == 0:
#         return 1
#     return fact_iter(n, 1)


# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num-1, num*product)


# print(fact(0))
# print(fact(1))
# print(fact(5))


# todo 汉诺塔问题

""" 
n 起始位置盘子数量
a,b,c应传入三个位置的名称
a 起始位置
b 中转位置
c 目标位置
"""


def move(n, a, b, c):
    if n == 1:
        print(a, '==>', c)
    else:
        move(n-1, a, c, b)
        print(a, '==>', c)
        move(n-1, b, a, c)


move(5, 'a', 'b', 'c')
