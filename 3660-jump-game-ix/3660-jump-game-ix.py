class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [nums[0] for _ in range(N)]
        for i in range(1, N):
            res[i] = max(res[i-1], nums[i])
        
        left = right = N - 1
        while left >= 0:
            while left < right and nums[right] >= res[left]:
                right -= 1
            res[left] = res[right]
            left -= 1
        
        return res
        
        
        