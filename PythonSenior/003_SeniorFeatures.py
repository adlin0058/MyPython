# 高级特性

# todo 构造一个1，3，5，7，。。。。99的列表

# L = []
# n = 1
# while n < 100:
#     L.append(n)
#     n += 2

# print(L)

L = [x for x in range(1, 100, 2)]
print(L)
