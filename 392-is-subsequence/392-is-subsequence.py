class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for ch in t:
            if len(s) > 0 and ch == s[0]:
                s = s[1:]
        return len(s) == 0