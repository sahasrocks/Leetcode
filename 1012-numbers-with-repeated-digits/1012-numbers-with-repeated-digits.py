class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        dp=[[[[[-1 for tight in range(2)] for i in range(2)] for i in range(2)] for i in range(2**10)] for i in range(10)]
        len1 = len(str(n))
        def fun(i,check,tight,memo,leading_zero):
            if i==len1:
                if check==1:
                    return 1
                return 0
            end = 9
            if dp[i][memo][check][leading_zero][tight]!=-1:
                return dp[i][memo][check][leading_zero][tight]
            if tight==1:
                end = int(str(n)[i])
            res = 0
            for j in range(end+1):
                if j==0 and leading_zero==1:
                    res+=fun(i+1,0,tight&(j==end),memo,1)
                    continue
                if check==1:
                    res+=fun(i+1,1,tight&(j==end),memo|(1<<j),0)
                    continue
                if memo&(1<<j):
                    res+=fun(i+1,1,tight&(j==end),memo,0)
                else:
                    res+=fun(i+1,0,tight&(j==end),memo|(1<<j),0)
            dp[i][memo][check][leading_zero][tight] = res
            return res
        return fun(0,0,1,0,1)