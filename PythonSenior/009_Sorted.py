
# # 默认从小到大
# l = [36, 5, -12, 9, -21]
# print(sorted(l))


# # 可以设置key
# print(sorted(l, key=abs))

# # 使用key忽略对字符串排序时的大小写
# l1 = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(l1, key=str.lower))
# # 反向排序
# l3 = sorted(l1, key=str.lower, reverse=True)
# print(l3)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def by_sorce(t):
    return t[1]


L3 = sorted(L, key=by_sorce, reverse=True)
print(L3)
