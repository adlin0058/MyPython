
# todo 冒泡排序

def BubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [22, 2, 26, 32, 82, 12]

BubbleSort(arr)
print(arr)
