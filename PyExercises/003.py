
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# for i in range(3):
#     nums1.pop()
# nums1 += nums2
# # s = set(nums1)
# # print(s)
# # nums1 = list(s)
# # print(nums1)
# nums1.sort()
# print(nums1)

# nums = [1, 2, 2, 2, 1, 1, 11, 1, 1]
# while 1 in nums:
#     nums.remove(1)

# print(nums)

# nums = [1, 1, 2]
# s = set(nums)
# nums = list(s)
# print(nums)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
""" 
0 1 1 2
"""
print(nums)
a, b = 0, 1
f = False
while b < len(nums):
    if nums[a] == nums[b]:
        if f == True:
            nums.pop(b)
        b += 1
        f = True
    else:
        a += 1
        b += 1
        f = False

print(nums)
