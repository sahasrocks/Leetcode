class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        minimum = float('inf')
        ind = 0
        while nums != sorted(nums):
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < minimum:
                    minimum = nums[i] + nums[i + 1]
                    ind = i
            nums.pop(ind)
            nums[ind] = minimum
            minimum, ind = float('inf'), 0
            res += 1
        return res