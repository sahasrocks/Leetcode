class Solution:
    def frequencySort(self, s: str) -> str:
        c1=Counter(s)
        c2=''
        n = sorted(s, key=lambda x: (c1[x], x), reverse=True)    
        for i in n:
            c2+=i
        return c2    
        