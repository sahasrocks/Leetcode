class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        res=0
        i=1
        nums.sort()
        if len(nums)<2:
            return 0
        for i in range(1,len(nums)):
            a= nums[i]-nums[i-1]
            res=max(res,a)
        return res    
        