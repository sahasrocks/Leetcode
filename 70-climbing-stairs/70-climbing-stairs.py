class Solution:
    def climbStairs(self, n: int) -> int:
        
        
    	# a, b = 1, 1
    	# for i in range(n): 
    	#     a, b = b, a + b
    	# return a
        # if n<=2:
        #     return n
        # return (self.climbStairs(n - 1) + self.climbStairs(n - 2))
        dp=[-1]*(n+1)
        for i in range(n+1):
            if i<=2:
                dp[i]=i
            else:
                dp[i]=dp[i-1]+dp[i-2]
        return dp[n]        