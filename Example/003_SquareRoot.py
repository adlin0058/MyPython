# 计算实数和复数的平方根

import cmath


num = float(input('请输入一个数字：'))
if num >= 0:
    num_sqrt = num**0.5
    print('%0.3f 的平方根为 %0.3f' % (num, num_sqrt))
else:
    num_sqrt = cmath.sqrt(num)
    print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
