class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] ==1:
            return 0
        dp=[[-1]*n for i in range(m)]
        def dfs(i,j):
            if i==(m-1) and j==n-1:
                return 1
            if i>=m or j>=n or obstacleGrid[i][j]:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i+1,j) + dfs(i,j+1)
            return dp[i][j]
        return dfs(0,0)                    
        
        
        # m=len(obstacleGrid)
        # n=len(obstacleGrid[0])
        # if obstacleGrid[m-1][n-1]==1:
        #     return 0
        # dp=[[0]*(n+1) for _ in range(m+1)]
        # dp[m-1][n-1]=1
        # for r in range(m-1,-1,-1):
        #     for c in range(n-1,-1,-1):
        #         if obstacleGrid[r][c]==1:
        #             dp[r][c]=0
        #         else:
        #             dp[r][c]+=dp[r+1][c]+dp[r][c+1]
        # return dp[0][0]                
        
        
        
        
        # m=len(obstacleGrid)
        # n=len(obstacleGrid[0])
        # if obstacleGrid[m-1][n-1]==1:
        #     return 0
        # dp=[[-1]*n for _ in range(m)]

        # def dfs(i,j):
        #     if i== (m-1) and j == (n-1):
        #         return 1
        #     if i >= m or j >= n or obstacleGrid[i][j]:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     dp[i][j] = dfs(i+1,j) + dfs(i,j+1)
        #     return dp[i][j]
        # return dfs(0,0)



        # if not obstacleGrid or obstacleGrid[0][0] == 1:
        #     return 0

        # rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [0] * cols
        # dp[0] = 1

        # for r in range(rows):
        #     for c in range(cols):
        #         if obstacleGrid[r][c] == 1:
        #             dp[c] = 0
        #         else:
        #             if c > 0:
        #                 dp[c] += dp[c - 1]

        # return dp[cols - 1] 