class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1]*n for i in range(m)]
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return grid[i][j]
            if i>=m or j>=n:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j]= grid[i][j] + min(dfs(i+1,j),dfs(i,j+1))
            return dp[i][j]
        return dfs(0,0)                
        # m,n=len(grid),len(grid[0])
        # dp=[[-1]*n for i in range(m)]
        # def dfs(i,j):
        #     if i==m-1 and j==n-1:
        #         return grid[i][j]
        #     if i>=m or j>=n:
        #         return float('inf')
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     dp[i][j] = grid[i][j] + min(dfs(i+1,j),dfs(i,j+1))
        #     return dp[i][j]
        # return dfs(0,0)                
        
        
        # ROWS, COLS = len(grid), len(grid[0])
        # dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        # dp[ROWS - 1][COLS] = 0

        # for r in range(ROWS - 1, -1, -1):
        #     for c in range(COLS - 1, -1, -1):
        #         dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        # return dp[0][0]        
        
        
        
        
        # m, n = len(grid), len(grid[0])
        # dp = [[-1] * n for _ in range(m)]

        # def dfs(r, c):
        #     if r == m - 1 and c == n - 1:
        #         return grid[r][c]
        #     if r == m or c == n:
        #         return float('inf')
        #     if dp[r][c] != -1:
        #         return dp[r][c]

        #     dp[r][c] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
        #     return dp[r][c]

        # return dfs(0, 0)                

        # def dfs(r, c):
        #     if r == len(grid) - 1 and c == len(grid[0]) - 1:
        #         return grid[r][c]
        #     if r == len(grid) or c == len(grid[0]):
        #         return float('inf')
        #     return grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))

        # return dfs(0, 0)            



        # get dimensions
        # n = len(grid) # no of cells in each col
        # m = len(grid[0]) # no of cells in each row
        
        # # populate first row using m for no of cells in row
        # for i in range(1,m):
        #     grid[0][i] = grid[0][i] + grid[0][i-1]
        
        # # populate first col using n for no of cells in col
        # for j in range(1,n):
        #     grid[j][0] = grid[j-1][0] + grid[j][0]
        
        # # populate the rest
        # for i in range(1,n):
        #     for j in range(1,m):
		# 		# get min seen so far plus curr cell value
        #         grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        
        # # return last cell
        # return grid[-1][-1]
        