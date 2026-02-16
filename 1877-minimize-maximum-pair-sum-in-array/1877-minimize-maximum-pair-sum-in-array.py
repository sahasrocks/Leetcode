class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        res=0
        while l<=r:
            a=nums[l]+nums[r]
            res=max(a,res)
            l+=1
            r-=1
        return res    
        
        # nums.sort()
        # l=0
        # r=len(nums)-1
        # res=0
        # while l<=r:
        #     a=nums[l]+nums[r]
        #     res=max(res,a)
        #     l+=1
        #     r-=1
        # return res    
        