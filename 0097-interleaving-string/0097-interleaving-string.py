class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp=[[False] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)]=True

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True

                if j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        return dp[0][0]            

        
        
        # dp={}
        # if len(s1)+len(s2) != len(s3):
        #     return False
        # def dfs(i,j):
        #     if len(s1)==i and j==len(s2):
        #         return True
        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
            
        #     if i<len(s1) and s1[i]==s3[i+j]:
        #         if dfs(i+1,j):
        #             return True
        #     if j<len(s2) and s2[j]==s3[i+j]:
        #         if dfs(i,j+1):
        #             return True
        #     dp[(i,j)]=False

        #     return False
        # return dfs(0,0) 
        
        
        # def dfs(i,j,k):
        #     if k==len(s3):
        #         return (i==len(s1) and j==len(s2))
        #     if i<len(s1) and s1[i]==s3[k]:
        #         if dfs(i+1,j,k+1):
        #             return True
        #     if j<len(s2) and s2[j]==s3[k]:
        #         if dfs(i,j+1,k+1):
        #             return True
        #     return False
        # return dfs(0,0,0)                        
        
        
        
        
        # n, m = len(s1), len(s2)
        # if n + m != len(s3): return False
        # dp = [True] * (m+1)
        # for i in range(1, m+1):
        #     dp[i] = dp[i-1] and s2[i-1] == s3[i-1]
        # for i in range(n):
        #     dp[0] = dp[0] and s1[i] == s3[i] 
        #     for j in range(m):
        #         dp[j+1] = (dp[j+1] and s1[i] == s3[i+j+1]) or (dp[j] and s2[j] == s3[i+j+1])
        # return dp[-1]