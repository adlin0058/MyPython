
# 简单计算器
def myAdd(x, y):
    return x+y


def mySubtract(x, y):
    return x-y


def myMultiply(x, y):
    return x+y


def myDivide(x, y):
    return x/y


print('计算方式：')
print('1：加法')
print('2：减法')
print('3：乘法')
print('4：除法')
switch = int(input('请选择计算方式：'))
x = int(input('请输入第一个数：'))
y = int(input('请输入第二个数：'))
if switch == 1:
    print(myAdd(x, y))
elif switch == 2:
    print(mySubtract(x, y))
elif switch == 3:
    print(myMultiply(x, y))
elif switch == 4:
    print(myDivide(x, y))
else:
    print('请选择正确的符号')
