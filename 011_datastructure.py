
#! 数据结构
# Python中列表是可变的，
# 这是它区别于字符串和元组的最重要的特点，
# 一句话概括即：列表可以修改，而字符串和元组不能

# todo 将列表当作堆栈使用
#! 后进先出
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

# todo 将列表当作队列使用
#! 先进先出
# from collections import deque
# queue = deque(['Eric', 'John', 'Michael'])
# queue.append('Terry')
# queue.append('Graham')
# queue.popleft()
# print(queue)
# queue.popleft()
# print(queue)
# queue.popleft()
# print(queue)
# queue.popleft()
# print(queue)

# todo 列表推导式
# vec = [2, 4, 6]
# vec1 = [3*x for x in vec]
# print(vec1)

# vec2 = [[x, x**2] for x in vec]
# print(vec2)

# freshfruit = ['   banana', '  loganberry ', 'passion fruit  ']
# vec3 = [weapon.strip() for weapon in freshfruit]
# print(vec3)

# vec1 = [2, 4, 6]
# vec2 = [4, 3, -9]
# rst1 = [x*y for x in vec1 for y in vec2]
# print(rst1)

# rst2 = [str(round(355/113, i)) for i in range(1, 6)]
# print(rst2)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# rst3 = [[row[i] for row in matrix] for i in range(4)]
# print(rst3)

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)
# del a[2:5]
# print(a)
# del a[:]
# print(a)
# del a

# 元组和序列
t = 12345, 54321, 'hello'
print(t[0])
print(t)

u = t, (1, 2, 3, 4, 5)
print(u)
