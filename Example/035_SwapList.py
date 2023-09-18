# 将列表中头尾两个元素对调

# def swap(arr):
#     n = len(arr)
#     arr[0], arr[n-1] = arr[n-1], arr[0]

#! 优化为
def swap(arr):
    arr[0], arr[-1] = arr[-1], arr[0]


arr = [1, 2, 3, 4]
swap(arr)
print(arr)
