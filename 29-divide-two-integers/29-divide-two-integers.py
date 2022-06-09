class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        import math
        c = dividend/divisor
        if c<0:
            d = math.ceil(c)
        else :
            d = math.floor(c)
        f = pow(2,31) -1 
        e = -pow(2,31)
        if d > f:
            d = f
        if d <e:
            d =e
        return d