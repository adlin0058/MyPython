
# 二分查找

def binarySearch(arr, l, r, x):

    if r >= l:
        mid = int(l + (r - l)/2)

        # 元素正好中间位置
        if arr[mid] == x:
            return mid

        # 元素小于中间位置的元素，只需要比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # 元素大于中间位置的元素，只需要比较右边的元素
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1


arr = [2, 3, 4, 10, 30]
x = 10

result = binarySearch(arr, 0, 4, x)

if result != -1:
    print('元素在数组中的索引是 %d' % result)
else:
    print('元素不在数组中')
