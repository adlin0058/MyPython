# 创建一个字典 d = {key:value,...}
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

print(d)

# 修改value
d['Bob'] = 80
print(d['Bob'])

# 判断key是否存在
print('Thomas' in d)

# get()方法，如果key不存在，返回None
print(d.get('Thomas'))
# 可以自定义返回值
print(d.get('Thomas', -1))  # key不存在时返回-1

# 删除一个key，pop(key)方法
d.pop('Bob')
print(d)
