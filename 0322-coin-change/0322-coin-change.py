class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)

        dp[0]=0
        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!=amount+1 else -1            
        
        
        
        
        
        
        
        
        # memo = {}
        
        # def check(amount):
        #     if amount in memo: return memo[amount]
        #     if amount == 0: return 0
        #     if amount < 0: return float("inf")
        #     memo[amount] = min([1 + check(amount - coin) for coin in coins])
        #     return memo[amount]
        
        # minimum = check(amount)
        # return minimum if minimum < float("inf") else -1