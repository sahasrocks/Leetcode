class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        left = right = start
        n = len(nums) - 1

        while nums[left] != target and nums[right] != target:
            if left > 0:
                left -= 1
            if right < n:
                right += 1

        return max(right - start, start - left)