class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        maxProfit= 0
        for i in prices:
            maxProfit = max(maxProfit,i-minVal)
            minVal = min(minVal,i)
        return maxProfit    