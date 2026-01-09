class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.bs(nums,target,True)
        right=self.bs(nums,target,False)
        return [left,right]
    
    def bs(self,nums,t,leftbias):
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            if t>nums[m]:
                l=m+1
            elif t<nums[m]:
                r=m-1
            else:
                i=m
                if leftbias:
                    r=m-1
                else:
                    l=m+1
        return i                        
    
    # def bs(self,nums,target,leftbias):
    #     l,r=0,len(nums)-1
    #     i=-1
    #     while l<=r:
    #         m=(l+r)//2
    #         if target>nums[m]:
    #             l=m+1
    #         elif target<nums[m]:
    #             r=m-1
    #         else:
    #             i=m
    #             if leftbias:
    #                 r=m-1
    #             else:
    #                 l=m+1
    #     return i                        
    
    
    
    
    
    #     left=self.bs(nums,target,True)
    #     right=self.bs(nums,target,False)
    #     return [left,right]
        
        
        
        
    # def bs(self,nums,target,leftbias):
    #     l,r=0,len(nums)-1
    #     i=-1
    #     while l<=r:
    #         m=(l+r)//2
    #         if target>nums[m]:
    #             l=m+1
    #         elif target<nums[m]:
    #             r=m-1
    #         else:
    #             i=m
    #             if leftbias:
    #                 r=m-1
    #             else:
    #                 l=m+1
    #     return i                            
        
        
        # if len(nums)==0:
        #     return [-1,-1]
        # l=[]
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         l.append(i)
        # if len(l)==0:
        #     return [-1,-1]
        # return [l[0],l[-1]]
                