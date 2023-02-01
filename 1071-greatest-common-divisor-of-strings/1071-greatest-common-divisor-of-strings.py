class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        for i in range(min(m, n), 0, -1):
            if n % i > 0 or m % i > 0: continue
                
            a, b = m // i, n // i
            test = str2[:i]
            if test * a == str1 and test * b == str2:
                return test
        
        return ''