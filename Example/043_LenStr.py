# 使用循环计算字符串长度

def strLen(s):
    cnt = 0
    while s[cnt:]:
        cnt += 1
    return cnt


s = 'daadas'
print(strLen(s))
