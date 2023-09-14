# 最小公倍数
# least common multiple

def myLcm(x, y):
    n = x if x > y else y
    while True:
        if (n % x == 0) and (n % y == 0):
            return n
        n += 1


l = myLcm(54, 24)
print(l)
