class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        def dfs(i,j):
            if i== (m-1) and j == (n-1):
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i+1,j) + dfs(i,j+1)
            return dp[i][j]
        return dfs(0,0)        
        
        
        
        
        
        
        # def dfs(i,j):
        #     if i== (m-1) and j == (n-1):
        #         return 1
        #     if i >= m or j >= n:
        #         return 0
        #     return dfs(i+1,j) + dfs(i,j+1)
        # return dfs(0,0)        

        
        
        #return ( factorial(m+n-2)//factorial(m-1) )//factorial(n-1)