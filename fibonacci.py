
# todo 斐波那契数列模块
#! use for 013_using_fibo,py
def fib1(n):  # 打印从0到n的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    rst = []
    a, b = 0, 1
    while b < n:
        rst.append(b)
        a, b = b, a+b
    return rst
