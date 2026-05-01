class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        # F(0)
        F = sum(i * num for i, num in enumerate(nums))
        res = F

        for k in range(1, n):
            F = F + total - n * nums[n - k]
            res = max(res, F)

        return res
        # a = [nums[i:] + nums[:i] for i in range(len(nums))]
        # res=float('-inf')
        # for t in a:
        #     z=0
        #     for i,e in enumerate(t):
        #         z+=e*i
        #     res=max(res,z)
        # return res        
