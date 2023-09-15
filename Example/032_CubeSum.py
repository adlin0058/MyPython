# 计算从1到n的立方和

def cubeSum(n):
    # sum = 0
    # for i in range(1, n+1):
    #     sum += i**3
    # return sum
    return (lambda n: sum([x**3 for x in range(n+1)]))(n)


print(cubeSum(int(input('请输入个数：'))))
