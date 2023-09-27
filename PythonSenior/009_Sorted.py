
# # 默认从小到大
# l = [36, 5, -12, 9, -21]
# print(sorted(l))


# # 可以设置key
# print(sorted(l, key=abs))

# # 使用key忽略对字符串排序时的大小写
# l1 = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(l1, key=str.lower))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)
