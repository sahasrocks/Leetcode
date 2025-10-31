class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(i):
        #     if i>=n:
        #         return i==n
        #     return dfs(i+1)+dfs(i+2)
        # return dfs(0)    
        # if n<=2:
        #     return n       
        # dp=[0]*(n+1)
        # dp[1],dp[2]=1,2
        # for i in range(3,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]            

        memo={1:1,2:2}
        def td(n):
            if n in memo:
                return memo[n]
            else:
                memo[n]= td(n-1)+td(n-2)
                return memo[n]
        return td(n)            

















    	# a, b = 1, 1
    	# for i in range(n): 
    	#     a, b = b, a + b
    	# return a
        # if n<=2:
        #     return n
        # return (self.climbStairs(n - 1) + self.climbStairs(n - 2))
        # dp=[-1]*(n+1)
        # for i in range(n+1):
        #     if i<=2:
        #         dp[i]=i
        #     else:
        #         dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]        
        