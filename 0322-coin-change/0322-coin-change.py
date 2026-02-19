class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp={}
        # def dfs(amount):
        #     if amount ==0:
        #         return 0
        #     if amount in dp:
        #         return dp[amount]
        #     res=1e9
        #     for coin in coins:
        #         if amount-coin>=0:
        #             res=min(res,1+dfs(amount-coin))
        #     dp[amount]=res
        #     return res
        # mincoin=dfs(amount)
        # return -1 if mincoin>=1e9 else mincoin                    
        
        
        # dp=[amount+1]*(amount+1)

        # dp[0]=0
        # for a in range(1,amount+1):
        #     for c in coins:
        #         if a-c>=0:
        #             dp[a]=min(dp[a],1+dp[a-c])
        # return dp[amount] if dp[amount]!=amount+1 else -1            
        
        
        
        
        
        
        
        
        # memo = {}
        
        # def check(amount):
        #     if amount in memo: return memo[amount]
        #     if amount == 0: return 0
        #     if amount < 0: return float("inf")
        #     memo[amount] = min([1 + check(amount - coin) for coin in coins])
        #     return memo[amount]
        
        # minimum = check(amount)
        # return minimum if minimum < float("inf") else -1
        # dp={}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if i==0:
        #         return 0
        #     if i<0:
        #         return float('inf')
        #     dp[i]=min([1+dfs(i-coin) for coin in coins])
        #     return dp[i]
        # mi=dfs(amount)
        # return mi if mi <float('inf') else -1
        dp={}
        def dfs(i):
            if i==0:
                return 0
            if i in dp:
                return dp[i]
            if i<0:
                return float('inf')
            dp[i] = min([1+dfs(i-coin) for coin in coins])
            return dp[i]
        mi= dfs(amount)                
        return mi if mi < float('inf') else -1
        # dp={}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if i==0:
        #         return 0
        #     if i<0:
        #         return float("inf")
        #     dp[i]=min([1 + dfs(i-coin) for coin in coins])
        #     return dp[i]
        # minimum=dfs(amount)
        # return minimum if minimum < float("inf") else -1                
