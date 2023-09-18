# 计算元素在列表中出现的次数

def Times(l, e):
    cnt = 0
    for x in l:
        if x == e:
            cnt += 1
    return cnt


l = [1, 2, 1, 1, 5, 6, 72, 8, 2]
print(Times(l, 1))
print(Times(l, 1))
print(Times(l, 99))


# 还可以直接使用count()方法
cnt = l.count(1)
print(cnt)
