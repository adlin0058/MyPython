# 阶乘
def factoral(n):
    if n < 0:
        print('负数没有阶乘')
    elif n == 0:
        print('0 的阶乘是1')
    else:
        f = 1
        for i in range(1, n+1):
            f = f*i
        print('%d 的阶乘为 %d' % (n, f))


factoral(0)
factoral(3)
factoral(10)
factoral(13)
