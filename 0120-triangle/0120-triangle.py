class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        dp=[[float('inf')]*m for i in range(m)]
        def dfs(i,j):
            if i>=m:
                return 0
            if dp[i][j] != float('inf'):
                return dp[i][j]
            dp[i][j] = triangle[i][j] + min(dfs(i+1,j),dfs(i+1,j+1))
            return dp[i][j]
        return dfs(0,0)            
        # memo = [[float("inf")] * len(triangle[r]) for r in range(len(triangle))]


        # def dfs(r,c):
        #     if r>=len(triangle):
        #         return 0
        #     if memo[r][c] != float("inf"):
        #         return memo[r][c]
        #     memo[r][c]=triangle[r][c] + min(dfs(r+1,c),dfs(r+1,c+1))
        #     return memo[r][c]
        # return dfs(0,0)            

        # def dfs(row,col):
        #     if row>=len(triangle):
        #         return 0
        #     return triangle[row][col] + min(dfs(row+1,col),dfs(row+1,col+1))     
        # return dfs(0,0)           
        
        
        
        # for level in range(1, len(triangle)):
        #     for i in range(level+1):
        #         triangle[level][i] += min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
        # return min(triangle[-1])