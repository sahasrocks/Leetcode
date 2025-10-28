class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res=0
        left=nums[0]
        for i in range(1,len(nums)-1):
            if (left<nums[i] and nums[i]>nums[i+1]) or ( left>nums[i] and nums[i]<nums[i+1] ):
                res+=1
                left=nums[i]
        return res        
