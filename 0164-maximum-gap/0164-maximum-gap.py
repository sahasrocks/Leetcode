class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        if len(nums)<2:
            return 0
        nums.sort()
        for i in range(len(nums)-1):
            dp[i]=nums[i+1]-nums[i]
        return max(dp)        
        # dp=[0]*len(nums)
        # if len(nums)<2:
        #     return 0
        # nums.sort()
        # for i in range(len(nums)-1):
        #     dp[i]=nums[i+1]-nums[i]
        # return max(dp)        
        
        
        
        # dp=[0]*len(nums)
        # if len(nums)<2:
        #     return 0
        # nums.sort()
        # for i in range(len(nums)-1):
        #     dp[i]=nums[i+1]-nums[i]
        # return max(dp)        
        
        # dp=[0]*len(nums)
        # if len(nums)<2:
        #     return 0
        # nums.sort()
        # for i in range(len(nums)-1):
        #     dp[i]=nums[i+1]-nums[i]
        # return max(dp)    
        
        # res=0
        # i=1
        # nums.sort()
        # if len(nums)<2:
        #     return 0
        # for i in range(1,len(nums)):
        #     a= nums[i]-nums[i-1]
        #     res=max(res,a)
        # return res    
        