
# 插入排序
def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [6, 2, 89, 2, 5]

insertSort(arr)

print(arr)
