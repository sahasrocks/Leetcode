class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bs(l,r):
            if l==r:
                return l
            m=l+(r-l)//2
            if nums[m]>nums[m+1]:
                return bs(l,m)
            return bs(m+1,r)
        return bs(0,len(nums)-1)
        
        
        
        
        # for i in range(len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         return i
        # return len(nums)-1        