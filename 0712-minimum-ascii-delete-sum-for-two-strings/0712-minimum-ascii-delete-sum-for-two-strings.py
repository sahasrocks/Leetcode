class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n,m,res = len(s1),len(s2),0
        dp = [0] * (m + 1)
        for i in s1 + s2: res += ord(i)
        for i in range(n):
            prev = 0
            for j in range(m):
                if s1[i] == s2[j]:
                    prev, dp[j+1] = dp[j+1], max(dp[j] , prev + ord(s1[i]))
                else:
                    prev, dp[j+1] = dp[j+1], max(dp[j+1] , dp[j])
        return res - (dp[-1] << 1)