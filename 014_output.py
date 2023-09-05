# s = 'hello world'
# print(str(s))
# print(repr(s))
# print(str(1/7))
# print(repr(1/7))


# todo 两种方式输出一个平方和立方的表
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#     print(repr(x*x*x).rjust(4))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#! 字符串方法
# str.rjust() str.ljust() str.center() str.zfill()
# 居右           居左         居中          左边填充0

# str.format(str1,str2)
print('{0}网址： "{1}!"'.format('菜鸟教程', 'www.runoob.com'))

# {}中的数字指向传入对象的位置
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))

# 可以使用关键字参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

# 位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
