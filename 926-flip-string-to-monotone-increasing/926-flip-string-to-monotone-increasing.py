class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        c1=0
        c0=0
        for i in range(len(s)):
            if s[i]=='0':
                c0+=1
            else:
                c1+=1
            
            if c0> c1:
                c0=c1
        return c0        