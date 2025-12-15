class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0 
        for i, x in enumerate(prices): 
            if i == 0 or prices[i-1] != x + 1: cnt = 0
            cnt += 1
            ans += cnt 
        return ans 