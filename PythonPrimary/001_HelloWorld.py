#!/usr/bin/env python3
# print('hello', ',', 'world')
# print(100+200)
# print(2**10)
# print('100 + 200 =', 100+200)

# name = input()
# print('you are so nice ,', name)

# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)
# print(10_000_000_000)
# print(0x9d90_2c)
# print('I\'m OK.')
# print(-280.74)
# print(1.23e9)
# print('\\\n\\')
# print(r'\\\t\\')
# print('''line1
# line2
# line3''')
# print(r'''hello\n
# world''')

# print(3 > 2)
# print(3 < 2)
# print(True and False)
# print(True or False)
# print(not True)
# print(False or False)

# age = int(input())
# if age >= 18:
#     print('adult')
# else:
#     print('teenager')


# a = 123
# b = 'char'
# c = True
# print(a, b, c)

# print(ord('A'))
# print(ord('中'))
# print(chr(66))
# print(chr(25991))


# print('\u4e2d\u6587')

# print('Hello , %s' % 'world')
# print('I have %d apple' % 12)
# print('PI = %.2f' % 3.1415926)
# # 转义 %%表示一个%
# print('growth rate: %d %%' % 70)
# # f-string
# r = 3.5
# s = 3.14 * r**2
# print(f'The area of a circle with radius {r} is {s:.2f}')

# # 格式化练习 小明的成绩从去年的72分提升到了今年的85分，
# # 请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，
# # 只保留小数点后1位：
# score_lastyear = 72
# score_thisyear = 85
# promotion = 100 * (score_thisyear - score_lastyear) / score_lastyear
# print(f'Ming\'s promotion is {promotion:.1f}%')
# print('Ming\'s promotion is %.1f%%' % promotion)

# 编码格式
# print('中文'.encode('utf-8'))
# s = 'Python-中文'
# print(s)
# b = s.encode('utf-8')
# print(b)
# print(b.decode('utf-8'))

print(chr(3))
print(chr(33))
print(chr(333))

a = 'ABC'.encode('ascii')
print(a)
print(a.decode('utf-8'))
