class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        a=sorted(s)
        b=sorted(t)       
        return a==b