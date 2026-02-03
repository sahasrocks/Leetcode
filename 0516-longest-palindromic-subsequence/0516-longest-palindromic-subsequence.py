class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp={}
        def dfs(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i]==s[j]:
                dp[(i,j)]=dfs(i+1,j-1)+2
            else:
                dp[(i,j)]=max(dfs(i+1,j),dfs(i,j-1))
            return dp[(i,j)]
        return dfs(0,len(s)-1)                        
        
        
        # dp={}
        # def dfs(i,j):
        #     if i>j:
        #         return 0
        #     if i==j:
        #         return 1
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if s[i]==s[j]:
        #         dp[(i,j)] = dfs(i+1,j-1)+2
        #     else:
        #         dp[(i,j)] = max(dfs(i+1,j),dfs(i,j-1))
        #     return dp[(i,j)]
        # return dfs(0,len(s)-1)                        
        
        # memo={}
        # def dfs(i,j):
        #     if i>j:
        #         return 0
        #     if i==j:
        #         return 1
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if s[i]==s[j]:
        #         memo[(i,j)] = dfs(i+1,j-1)+2
        #     else:
        #         memo[(i,j)] = max(dfs(i+1,j),dfs(i,j-1))
        #     return memo[(i,j)]
        # return dfs(0,len(s)-1)                        
        
        
        # rev_s = s[::-1]
        # dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        # for i in range(1, len(s)+1):
        #     for j in range(1, len(s)+1):
        #         if s[i-1] == rev_s[j-1]:
        #             dp[i][j] = 1 + dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # return dp[-1][-1]