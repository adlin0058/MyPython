# 杨辉三角

def triangles(n):
    yang = []
    i = 0  # 第i层
    while i < n:
        j = 0  # 第i层的第j个元素
        hang = []  # 第j行的元素
        while j <= i:
            if j == 0 or j == i:
                hang.append(1)
            else:
                hang.append(yang[i-1][j-1]+yang[i-1][j])
            j += 1
        yang.append(hang)
        i += 1
    return yang


y = triangles(5)
for x in y:
    print(x)
