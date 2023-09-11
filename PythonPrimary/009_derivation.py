import math

#! 列表推导式
# todo 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母

names = ['Bob', 'Tom', 'Alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper()for name in names if len(name) > 3]
print(new_names)

# todo 计算 30 以内可以被 3 整除的整数
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

#! 字典推导式
# todo 将列表中各字符串值为键，各字符串的长度为值，组成键值对
listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {key: len(key) for key in listdemo}
print(newdict)

# todo 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)

#! 集合推导式
newset = {i**2 for i in (1, 2, 3)}
print(newset)

a = {x for x in 'adnaiushdasdse' if x not in 'abc'}
print(a)

#! 元组推导式
a = (x for x in range(1, 10))
# 返回的是生成器对象
print(a)
# 使用tuple()函数可以将生成器对象转换成元组
print(tuple(a))


list1 = ['python', 'test1', 'test2']
list2 = [word.title()
         if word.startswith('p')
         else word.upper()
         for word in list1]
print(list2)
