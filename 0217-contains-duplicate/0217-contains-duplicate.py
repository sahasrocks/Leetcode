class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        """
        a=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                a+=1
        return a!=0        
        