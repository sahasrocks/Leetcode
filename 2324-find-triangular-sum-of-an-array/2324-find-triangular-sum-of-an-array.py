class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res, nCr, n = 0, 1, len(nums) - 1
        for r, num in enumerate(nums):
            res = (res + num  * nCr) % 10
            nCr = nCr * (n - r) // (r + 1)
        return res
# class Solution:
#     def triangularSum(self, nums: List[int]) -> int:
#         n=len(nums)
#         while n>0:
#             for i in range(n-1):
#                 nums[i]=(nums[i]+nums[i+1])%10
#             n-=1
#         return nums[0]