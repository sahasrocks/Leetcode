class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        cnt = 0
        ans = 0
        i = 0
        while i < n:
            if s[i] == '0':
                ans += cnt
                while i < n and s[i] != '1':
                    i += 1
            cnt += 1
            i += 1
        return ans