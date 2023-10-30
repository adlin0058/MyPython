
def productExceptSelf(nums):

    ans, tmp = [1] * len(nums), 1

    for i in range(1, len(nums)):

        ans[i] = ans[i - 1] * nums[i - 1]  # 下三角

    for i in range(len(nums) - 2, -1, -1):

        tmp *= nums[i + 1]                # 上三角

        ans[i] *= tmp                     # 下三角 * 上三角

    return ans


nums = [2, 5, 7, 1, 4]
rst = productExceptSelf(nums)
print(rst)
