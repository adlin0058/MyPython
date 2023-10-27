
# L = [2, 5, 7, 4]
# L.sort(reverse=False)

# print(L)
# print(L[:2])


# def twoSum(nums: list(int), target: int):
#     dic = {}
#     for i, x in enumerate(nums):
#         for j in range(i+1, len(nums)):
#             if x + nums[j] == target:
#                 return [i, j]


def twoSum(nums, target):
    dic = {}

    for i, x in enumerate(nums):
        complement = target - x
        if complement in dic:
            return [dic[complement], i]
        dic[x] = i

    return []


nums = [2, 7, 11, 15]
l = twoSum(nums, 9)
print(l)
