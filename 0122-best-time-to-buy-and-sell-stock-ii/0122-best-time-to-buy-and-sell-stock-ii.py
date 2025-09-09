class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curh=-float('inf')
        curnh=0
        for stock in prices:
            preh=curh
            prenh=curnh
            curh=max(preh,prenh-stock)
            curnh=max(prenh,preh+stock)
        return curnh    
