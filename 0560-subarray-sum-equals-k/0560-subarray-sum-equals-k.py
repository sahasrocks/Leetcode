class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        curSum=0
        preSum={0:1}

        for n in nums:
            curSum+=n
            diff = curSum-k
            res+=preSum.get(diff,0)

            preSum[curSum]=1 + preSum.get(curSum,0)
        return res    
        
        
        # res=0
        # for i in range(len(nums)):
        #     c=0
        #     for j in range(i,len(nums)):
        #         c+=nums[j]
        #         if c==k:
        #             res+=1
        # return res            
