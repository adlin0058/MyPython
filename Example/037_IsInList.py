# 判断元素是否在列表中

def isIn(l, e):
    if e in l:
        print('元素 {0} 在 {1} 中'.format(e, l))
    else:
        print('元素 {0} 不在 {1} 中'.format(e, l))


l = [1, 2, 3, 4, 5]
isIn(l, 1)
isIn(l, 6)
