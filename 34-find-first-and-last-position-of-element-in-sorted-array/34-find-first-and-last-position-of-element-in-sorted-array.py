class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        if len(l)==0:
            return [-1,-1]
        return [l[0],l[-1]]
                