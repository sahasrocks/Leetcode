class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p=0
        minb = prices[0]
        for i in prices:
            p = max(p,i-minb)
            minb=min(minb,i)
        return p    
        