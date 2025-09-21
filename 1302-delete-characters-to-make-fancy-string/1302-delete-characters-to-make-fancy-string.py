class Solution:
    def makeFancyString(self, s: str) -> str:
        res=[]
        for ch in s:
            if len(res)>=2 and  res[-1] ==res[-2] == ch:
                continue
            res.append(ch)
        return "".join(res)                
        