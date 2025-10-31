class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        while l<=r:
            m=(l+r)//2
            if m*m>x:
                r=m-1
            elif m*m<x:
                l=m+1
            else:
                return m
        return r
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # lo, hi = 0, x
        
        # while lo <= hi:
        #     mid = (lo + hi) // 2
            
        #     if mid * mid > x:
        #         hi = mid - 1
        #     elif mid * mid < x:
        #         lo = mid + 1
        #     else:
        #         return mid
        # return hi    