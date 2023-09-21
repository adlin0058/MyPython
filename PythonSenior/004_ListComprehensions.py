# 列表生成器
# L1 = list(range(1, 11))
# print(L1)

# L2 = list(range(1, 11, 2))
# print(L2)

# L3 = list(x*x for x in range(1, 11))
# print(L3)

# L4 = list(x*x for x in range(1, 11) if x % 2 == 0)
# print(L4)

# L5 = [m+n for m in 'ABC' for n in 'XYZ']
# print(L5)

# import os
# file_name = [d for d in os.listdir('.')]
# print(file_name)


# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k, v in d.items():
#     print(k, '=', v)

# L = ['Hello', 'World', 'IBM', 'Apple']
# L1 = [s.lower() for s in L]
# print(L1)


#! 列表生成器中使if else
L = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L)

# todo 将列表中的字母变成大写
L = ['Hello', 'World', 18, 'Apple', None]
rst = [s.upper() for s in L if isinstance(s, str)]
print(rst)
