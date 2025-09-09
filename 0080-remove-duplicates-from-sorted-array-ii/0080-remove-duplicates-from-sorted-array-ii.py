class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # j=1
        # for i in range(1,len(nums)):
        #     if j==1 or nums[i] != nums[j-2]:
        #         nums[j]=nums[i]
        #         j+=1
        # return j
        i = 2   # start from index 2, because first two elements are always allowed
        while i < len(nums):
            if nums[i] == nums[i-2]:
                nums.pop(i)   # remove the 3rd+ duplicate
            else:
                i += 1
        return len(nums)                
                    
        