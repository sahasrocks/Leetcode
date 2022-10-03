class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        prev = s[0]
        fee = local_sum = local_max = 0
        for cur, cur_cost in zip(s, cost):
            if cur == prev:
                local_sum += cur_cost
                local_max = max(cur_cost, local_max)
            else:
                fee += local_sum - local_max
                local_sum = cur_cost
                local_max = cur_cost
                prev = cur
        return fee + local_sum - local_max