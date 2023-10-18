
# todo 选择排序

def SelectSort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):

            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [6, 16, 26, 46, 66, 96]
SelectSort(arr)
print(arr)
