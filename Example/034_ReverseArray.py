# 反转数组指定个数的元素

# 使用列表删除和添加
def rvsArray(arr, d):
    for i in range(2):
        temp = arr.pop(0)
        arr.append(temp)


# 利用列表截取和拼接
def rvsArray2(arr, d):
    arr = arr[d:] + arr[:d]
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
arr1 = rvsArray2(arr, 2)
print(arr1)
