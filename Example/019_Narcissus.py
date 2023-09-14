# 水仙花数/阿姆斯特朗数
# 一个 n 位正整数等于其各位数字的 n 次方之和

#! 默认三位数
# def isNarrcissus(n):
#     cnt = 3
#     n1 = n // 100
#     n2 = (n//10) % 10
#     n3 = n % 10
#     print(n1, n2, n3)
#     if (n1**cnt + n2**cnt + n3**cnt) == n:
#         print('%d 是水仙花数' % n)
#     else:
#         print( '%d 不是水仙花数' % n)

#! 任意为数
def isNarrcissus(num):
    n = num
    l = len(str(n))
    sum = 0
    while n != 0:
        sum += (n % 10)**l
        n //= 10
    if sum == num:
        print('yes')
    else:
        print('no')


isNarrcissus(407)
