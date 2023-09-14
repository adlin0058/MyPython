
# todo  十进制、二进制、八进制、十六进制

dec = int(input('请输入一个十进制数:'))

print('转换为二进制为：', bin(dec))
print('转换成八进制为：', oct(dec))
print('转换成十六进制为：', hex(dec))

# todo ASCII、字符项目转换

c = input('请输入一个字符：')
a = int(input('请输入一个ASCII码：'))
print(c, '的ASCII码是：', ord(c))
print(a, '对应的字符为：', chr(a))
