class Solution:

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * k for _ in range(n)]
        s = 0
        for j in range(n):
            s += grid[0][j]
            dp[j][s % k] = 1
        for i in range(1, m):
            # Case of first column
            memo = [v for v in dp[0]] # Because not 3D dp array
            curr = grid[i][0]
            for ind in range(k):
                dp[0][(ind + curr) % k] = memo[ind] % MOD
            # Case of other columns
            for j in range(1, n):
                memo = [v for v in dp[j]] # Because not 3D dp array 
                curr = grid[i][j]
                for ind in range(k):                    
                    dp[j][(ind + curr) % k] = (memo[ind] + dp[j - 1][ind]) % MOD
        
        return dp[-1][0]