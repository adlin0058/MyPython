
from functools import reduce
nums = [1, 2, 3, 4, 5]
n = len(nums)
answer = [1]*n
for i in range(n):
    sum = 1
    tmp = nums[i]
    nums[i] = 1
    sum = reduce(lambda x, y: x*y, nums)
    answer[i] = sum
    nums[i] = tmp


print(answer)
# for x in answer:
#     print(x)


# L = [1, 2, 3, 4, 5]
# a = reduce(lambda x, y: x*y, L)
# print(a)
# # for x in L1:
# #     print(x)
