class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r= sum(weights)
        res=r

        def canShip(cap):
            ships,curCap=1,cap
            for w in weights:
                if curCap - w <0:
                    ships+=1
                    curCap = cap
                curCap-=w
            return ships <= days
        while l<=r:
            cap=(l+r)//2
            if canShip(cap):
                res= min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res                        
        
        
        
        
        
        
        
        # def count(capacity):
        #     sm=0
        #     day=0
        #     for i in range(len(weights)):
        #         if weights[i]+sm<=capacity:
        #             sm += weights[i]
        #         else:
        #             sm=0
        #             sm += weights[i]
        #             day += 1
        #     if(sm>0):
        #         day += 1
        #     return day<=days

        # start = max(weights)
        # end = sum(weights)
        # minCap = 0
        
        # while start<=end:
        #     mid = start + (end-start)//2
        #     if count(mid):
        #         minCap = mid
        #         end = mid-1
        #     else:
        #         start = mid+1
        
        # return minCap