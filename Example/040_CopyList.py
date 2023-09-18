# 复制列表

l = [1, 2, 34, 5]
l2 = l.copy()

print(l)
print(l2)


# 也可以使用列表拼接

def copyList(l):
    l2 = l[:]
    return l2


l = [1, 2, 4, 5]
print(l)
l2 = copyList(l)
print(l2)
