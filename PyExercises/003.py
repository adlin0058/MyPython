
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

nums = [1, 1, 1, 2, 2, 3]
""" 
0 1 1 2
"""
print(nums)
slow = 0
for fast in range(len(nums)):
    if slow < 2 or nums[slow-2] != nums[fast]:
        nums[slow] = nums[fast]
        slow += 1

print(slow)

print(nums)
