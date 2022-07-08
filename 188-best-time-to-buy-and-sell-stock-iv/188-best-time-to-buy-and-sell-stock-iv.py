class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0:
            return 0
        if len(prices)==0:
            return 0
        if (k>len(prices)/2):
            profit =0
            prices.append(0)
            for price, next_price in zip(prices[0:-1],prices[1:]):
                profit += max(0, next_price - price)
            return profit

        costs = [float('inf')] * k
        profits = [0] * k
        
        for p_ind, price in enumerate(prices):
            for i in range(min(k, (p_ind) // 2 + 1)):
                if(i == 0):
                    costs[i] = min(costs[i], price)
                else:
                    costs[i] = min(costs[i], price - profits[i-1])

                profits[i] = max(profits[i], price - costs[i])

        return max(profits)
            