class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if m>0 and nums[m]<nums[m-1]:
                r=m-1
            elif m<len(nums)-1 and nums[m]<nums[m+1]:
                l=m+1
            else:
                return m        
        
        
        
        
        
        
        # l,r=0,len(nums)-1
        # while l<=r:
        #     m=(l+r)//2
        #     if m>0 and nums[m]<nums[m-1]:
        #         r=m-1
        #     elif m<len(nums)-1 and nums[m]<nums[m+1]:
        #         l=m+1
        #     else:
        #         return m        
        
        
        # l,r=0,len(nums)-1
        # while l<=r:
        #     m=(l+r)//2
        #     if m>0 and nums[m]<nums[m-1]:
        #         r=m-1
        #     elif m<len(nums)-1 and nums[m]<nums[m+1]:
        #         l=m+1
        #     else:
        #         return m        
        
        # l,r=0,len(nums)-1
        # while l<=r:
        #     m=(l+r)//2
        #     if m>0 and nums[m]<nums[m-1]:
        #         r=m-1
        #     elif m<len(nums)-1 and nums[m]<nums[m+1]:
        #         l=m+1
        #     else:
        #         return m        
        
        # l,r=0,len(nums)-1
        # while l<=r:
        #     m=(l+r)//2
        #     if m>0 and nums[m] < nums[m-1]:
        #         r=m-1
        #     elif m<len(nums)-1 and nums[m]<nums[m+1]:
        #         l=m+1
        #     else:
        #         return m        

        
        
        # def bs(l,r):
        #     if l==r:
        #         return l
        #     m=(l+r)//2
        #     if nums[m]>nums[m+1]:
        #         return bs(l,m)
        #     return bs(m+1,r)
        # return bs(0,len(nums)-1)
        
        
        
        
        # for i in range(len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         return i
        # return len(nums)-1        