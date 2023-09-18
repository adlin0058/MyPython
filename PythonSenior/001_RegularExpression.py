# 正则表达式

# 匹配以数字开头，并以abc结尾的字符串
import re
#! 使用r前缀，不考虑转义
s = r'ABC\-001'

# re.match(正则表达式,带匹配字符串)
# 如果匹配返回一个Match对象,否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$', '021-12345'))


test = '用户输入字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')


#! 切分字符串
# \s匹配一个空白符
# \s+ 匹配一个或以上空白符
print(re.split(r'\s+', 'a   b    c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c   ,d'))


#! 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '021-12345')
print(m)
# 提取子串
print(m.group(0))
print(m.group(1))
print(m.group(2))

# todo 识别合法的时间
t = '3:33:33'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m)
print(m.groups())
