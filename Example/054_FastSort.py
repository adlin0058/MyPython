
# todo 快速排序

# 划分数组，并返回基准元素的索引
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# 快速排序函数


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = [66, 16, 96, 26, 6, 46]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)
