class Solution:
    def maximumScore(self, nums: List[int], mult: List[int]) -> int:
        n, m = len(nums), len(mult)
        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                right = n - 1 - i + left
                dp[i][left] = max(mult[i] * nums[left] + dp[i + 1][left + 1], 
                                  mult[i] * nums[right] + dp[i + 1][left])

        return dp[0][0]
        