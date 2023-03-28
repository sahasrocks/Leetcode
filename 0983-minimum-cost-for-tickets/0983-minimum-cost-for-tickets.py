

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # to speed up element checking for days
        travel_days = set(days)
        
        # ---------------------------------------------------
        
        # use python built-in cache as memoization for DP
        @cache
        def dp(day_d):
            
            ## Base case
            if day_d == 0:
                
                # no cost on before traveling
                return 0
            
            ## General cases
            if day_d not in travel_days:
                
                # no extra cost on non-traverl day
                return dp(day_d-1)
            
            else:
                
                # compute minimal cost on travel day
                
                with_1_day_pass = dp( day_d-1 ) + costs[0]
                with_7_day_pass = dp( max( day_d - 7, 0) ) + costs[1]
                with_30_day_pass = dp( max( day_d - 30, 0) ) + costs[2]
                
                return min( with_1_day_pass, with_7_day_pass, with_30_day_pass)
            
        # ---------------------------------------------------
        last_travel_day = days[-1]
        
        return dp(last_travel_day)
        