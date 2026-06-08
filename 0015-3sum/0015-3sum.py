class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for i,e in enumerate(nums):
            if e>0:
                break
            if i>0 and e==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                ts=e+nums[l]+nums[r] 
                if ts<0:
                    l+=1
                elif ts>0:
                    r-=1
                else:
                    res.append([e,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res                           