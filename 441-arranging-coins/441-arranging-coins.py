class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        if n==1:return 1
        while(n>=i):
            n=n-i
            i+=1
        return (i-1)
            