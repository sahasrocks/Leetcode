class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curmin=nums[0]
        curmax=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            temp=curmax
            curmax=max(n,n*curmax,n*curmin)
            curmin=min(n,n*temp,n*curmin)
            res=max(res,curmax)
        return res    
        
        # res=nums[0]
        # for i in range(len(nums)):
        #     cur=nums[i]
        #     res=max(res,cur)
        #     for j in range(i+1,len(nums)):
        #         cur*=nums[j]
        #         res=max(res,cur)
        # return res        

        
        
        
        
        
        
        
        
        
        
        
        
        
        # minval = nums[0]
        # maxval = nums[0]

        # currmax = nums[0]
        # if len(nums)==1:
        #     return currmax


        # for x in range(1 , len(nums)):
        #     if nums[x]<0:
        #         tmp = minval
        #         minval = maxval
        #         maxval = tmp

        #     minval  = min(nums[x] , nums[x]*minval)
        #     maxval = max(nums[x] , nums[x]*maxval)

        #     currmax = max(currmax , maxval)



        # return(currmax)