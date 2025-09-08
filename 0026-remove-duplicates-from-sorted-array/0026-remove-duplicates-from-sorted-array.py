class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # j=0
        # for i in range(1,len(nums)):
        #     if nums[j] !=nums[i]:
        #         j+=1
        #         nums[j] = nums[i]
        # return j+1        
        i=1
        while i <len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)         
