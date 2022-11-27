class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[defaultdict(int), defaultdict(int)] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][0][d] += 1
                dp[i][1][d] += dp[j][0][d] + dp[j][1][d]
        return sum(map(lambda x: sum(x[1].values()), dp))
        