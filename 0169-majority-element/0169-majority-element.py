class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n=0
        # maj=None
        # for num in nums:
        #     if n==0:
        #         maj= num
        #     n +=1 if maj ==num else -1
        # return maj        
        a=nums.sort()
        return nums[len(nums)//2]