
# todo 两个数的最大公约数
# greatest common divisor

def myGcd(x, y):
    n = x if x < y else y
    for i in range(n, 0, -1):
        if (x % i == 0) and (y % i == 0):
            return i


# n1 = int(input('请输入第一个数：'))
# n2 = int(input('请输入第二个数：'))

# print('两个数的最大公约数是：', gcd(n1, n2))

# todo 多个数的最大公约数
list = list(map(int, input('请输入几个数').split()))


def gcds(list):
    if list == []:
        return
    else:
        Min = min(list)
        rst = 0
        for i in list:
            m = myGcd(Min, i)
            if rst <= m:
                rst = m
        return rst


print('这几个数的最大公约数是：', gcds(list))
