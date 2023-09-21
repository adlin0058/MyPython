# 合并字典

# 使用update()
dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}

# dict1.update(dict2)
# print(dict1)


def merge(dict1, dict2):
    rst = {**dict1, **dict2}
    return rst


print(merge(dict1, dict2))
