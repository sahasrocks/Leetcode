class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minbuy=prices[0]
        for i in prices:
            profit=max(profit,i-minbuy)
            minbuy=min(minbuy,i)
        return profit    
        
        
        # profit=0
        # minBuy=prices[0]
        # for i in prices:
        #     profit=max(profit,i-minBuy)
        #     minBuy=min(minBuy,i)
        # return profit    

        
        
        
        
        
        
        
        # p=0
        # minb=prices[0]
        # for i in prices:
        #     p=max(p,i-minb)
        #     minb=min(minb,i)
        # return p    
        