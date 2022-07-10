class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i # only save the most recently index
        return False