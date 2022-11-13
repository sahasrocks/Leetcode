
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # from collections import Counter
        # c = Counter(nums)
        # c.most_common()
        # value, count = c.most_common()[0]
        # return value
        a=nums.sort()
        return nums[len(nums)//2]