class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        res=0
        l=0
        for r in range(len(nums)):
            count[nums[r]]+=1
            while count[nums[r]]>k:
                count[nums[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res        

        
        
        
        
        
        
        
        
        
        
        
        
        # freq = defaultdict(int)
        # ans = ii = 0
        # for i, x in enumerate(nums): 
        #     freq[x] += 1
        #     while freq[x] > k: 
        #         freq[nums[ii]] -= 1
        #         ii += 1
        #     ans = max(ans, i-ii+1)
        # return ans 
        