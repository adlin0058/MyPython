# 计算数组元素之和

def listSum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


l = [1, 2, 5, 7, 8]
print(listSum(l))
print(sum(l))
