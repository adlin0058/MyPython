# 计算圆的面积

def Area(r):
    PI = 3.14
    return PI*r*r


r = float(input('请输入圆的半径:'))
area = Area(r)
print('圆的面积为：%0.2f' % area)
