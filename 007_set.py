# 创建一个set s = set([1,2,3,...])
# s = set([1, 2, 3])
# print(s)

# set会自动过滤重复的元素
# s = set([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3])
# print(s)

# 可以通过add(key)添加元素到set中，可重复添加，但无效果
# s.add(4)
# print(s)
# s.add(4)
# print(s)

# 可以通过remove(key)方法删除元素
# s.remove(4)
# print(s)

# set可看作数学上无序无重复的集合，所以可以进行交际、并集操作
# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)

# 将两个可变对象放入set
s = ([1, 2, 3], [4, 5, 6], [1, 2, 3])
print(s)
