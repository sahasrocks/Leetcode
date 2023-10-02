class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=1
        for i in nums:
            if i!=0:
                res=res*i
        
        if 0 in nums:
            if nums.count(0)>1:
                return [0]*len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i]!=0:
                        nums[i]=0
                    else:
                        nums[i]=res
        else:
            for i in range(len(nums)):
                nums[i]=res//nums[i]
        return nums        