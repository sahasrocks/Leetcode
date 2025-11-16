class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9 +7
        res=0
        con=0
        for c in s:
            if c=="1":
                con+=1
                res=(res+con)%mod
            else:
                con=0
        return res            