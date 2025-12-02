class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            if nums[l]<=nums[m]:
                if target>nums[m] or target<nums[l]:
                    l=m+1
                else:
                    r=m-1
            else:
                if target < nums[m] or target> nums[r]:
                    r=m-1
                else:
                    l=m+1
        return -1                                
        
        
        
        
        # l,r=0,len(nums)-1
        # while l<=r:
        #     mid=(l+r)//2
        #     if nums[mid]==target:
        #         return mid
        #     #left sorted arr
        #     if nums[l]<=nums[mid]:
        #         if target >nums[mid] or target<nums[l]:
        #             l=mid+1
        #         else:
        #             r=mid-1
        #     else:
        #         if target<nums[mid] or target>nums[r]:
        #             r=mid-1
        #         else:
        #             l=mid+1
        # return -1                                
        
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1