class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        @cache
        def dp(n):
            if n > high: return 0
            c = int(low <= n <= high) + dp(n + zero) + dp(n + one)
            return c % (10**9 + 7)
        
        return dp(0)