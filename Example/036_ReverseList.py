# 反转列表


# revesed返回的是一个反转过的迭代器
# 需要将类型转换成list才可使用
def rvsList(l):
    return list(reversed(l))


l = [1, 2, 3, 4]

print(rvsList(l))
