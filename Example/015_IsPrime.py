# 判断质数
prime = []


def isPrime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                print('%d 不是质数' % n)
                return
        print('%d 是质数' % n)
        prime.append(n)
    else:
        print('%d 不是质数' % n)


max = input('请输入上限：')
try:
    Max = int(max) + 1
    for n in range(0, Max):
        isPrime(n)
    print('质数有：', prime)
except Exception:
    print('输入错误')
