class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=1
        m=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                m+=1
            else:
                res=max(res,m)
                m=1
            
        return max(res,m)        

        