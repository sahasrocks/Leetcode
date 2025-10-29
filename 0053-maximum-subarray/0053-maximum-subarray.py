class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=0
        maxSum=nums[0]
        for n in nums:
            if curSum<0:
                curSum=0
            curSum+=n
            maxSum=max(maxSum,curSum)
        return maxSum        
        
        
        
        # maxsum = cursum = nums[0]
        # for i in range(1,len(nums)):
        #     if cursum<0:
        #         cursum=nums[i]
        #     else:
        #         cursum +=nums[i]
        #     maxsum = max(maxsum,cursum)
        # return maxsum    
                
        