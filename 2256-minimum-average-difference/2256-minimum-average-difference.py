class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        leftsum = 0
        min_diff = float("inf")
        res = 0
        for i, val in enumerate(nums):
            leftsum += val
            avg1 = leftsum//(i+1)
            avg2 = 0 if i==n-1 else (s-leftsum)//(n-i-1)
            abs_diff = abs(avg1 - avg2)
            if abs_diff < min_diff:
                min_diff = abs_diff
                res = i
        return res