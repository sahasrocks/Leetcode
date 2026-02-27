class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z = s.count('0')  
        n = len(s)
        o = n - z         
        
        if z == 0:
            return 0
        
        for i in range(1, n + 1):  
            p = i * k
            if (p - z) % 2 != 0:
                continue
            if i % 2 == 1: 
                if p >= z and p <= (z * i + o * (i - 1)):
                    return i
            else:           
                if p >= z and p <= (z * (i - 1) + o * i):
                    return i
        
        return -1