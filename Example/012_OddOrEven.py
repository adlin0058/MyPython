# 判断奇数偶数

def OddOrEven(n):
    if (n % 2 == 0):
        print('这个数是偶数')
    else:
        print('这个数是奇数')


n = int(input('输入一个数：'))
OddOrEven(n)
