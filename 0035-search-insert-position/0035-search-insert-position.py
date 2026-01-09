class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return l                
        
        # l=0
        # r=len(nums)-1
        # while l<=r:
        #     mid=(l+r)//2
        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]>target:
        #         r=mid-1
        #     else:
        #         l=mid+1
        # return l                

        
        
        
        # nums.append(target)
        # nums.sort()
        # return nums.index(target)
        