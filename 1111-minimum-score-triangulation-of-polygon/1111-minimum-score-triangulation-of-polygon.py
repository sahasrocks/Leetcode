# class Solution:
#     def minScoreTriangulation(self, values: list[int]) -> int:
#         n = len(values)
#         dp = [[0]*n for _ in range(n)]
#         for length in range(2, n):
#             for i in range(n - length):
#                 j = i + length
#                 best = float('inf')
#                 for k in range(i + 1, j):
#                     s = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
#                     best = min(best, s)
#                 dp[i][j] = best
#         return dp[0][n - 1]

from functools import lru_cache

class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)

        @lru_cache(None)
        def dfs(i, j):
            # Base case: fewer than 3 vertices → no triangle
            if j - i < 2:
                return 0
            best = float("inf")
            for k in range(i+1, j):
                score = values[i] * values[k] * values[j]
                score += dfs(i, k) + dfs(k, j)
                best = min(best, score)
            return best

        return dfs(0, n-1)
