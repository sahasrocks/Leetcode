class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = (sum(nums) - 2 * sum(set(nums))) * -1

        for i in nums:    
            if s - i in nums:
                return[i, s-i]