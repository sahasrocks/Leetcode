class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rights=sum(nums)
        lefts=0
        ans=[0]*len(nums)
        for i in range(len(nums)):
            rights-=nums[i]
            ans[i]=abs(lefts-rights)
            lefts+=nums[i]
        return ans      