class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])

        # dp[r][c][cost] = max score
        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]

        # starting cell
        start_cost = 1 if grid[0][0] > 0 else 0
        if start_cost <= k:
            dp[0][0][start_cost] = grid[0][0]

        for r in range(m):
            for c in range(n):
                for cost in range(k+1):
                    if dp[r][c][cost] == -1:
                        continue

                    # try moving right
                    if c + 1 < n:
                        new_cost = cost + (grid[r][c+1] > 0)
                        if new_cost <= k:
                            dp[r][c+1][new_cost] = max(
                                dp[r][c+1][new_cost],
                                dp[r][c][cost] + grid[r][c+1]
                            )

                    # try moving down
                    if r + 1 < m:
                        new_cost = cost + (grid[r+1][c] > 0)
                        if new_cost <= k:
                            dp[r+1][c][new_cost] = max(
                                dp[r+1][c][new_cost],
                                dp[r][c][cost] + grid[r+1][c]
                            )

        # answer = best among all valid costs at destination
        res = max(dp[m-1][n-1])
        return res if res != -1 else -1
# class Solution:
#     def maxPathScore(self, grid: List[List[int]], k: int) -> int:
#         m,n=len(grid),len(grid[0])
#         def dfs(r,c,cost):
#             if r==m or c==n:
#                 return -1
#             costnew=cost+int(grid[r][c]>0)
#             if costnew>k:
#                 return -1
#             if r==m-1 and c==n-1:
#                 return grid[r][c]
#             score=max(dfs(r+1,c,costnew),dfs(r,c+1,costnew))
#             return score+grid[r][c] if score>=0 else -1
#         return dfs(0,0,0)                