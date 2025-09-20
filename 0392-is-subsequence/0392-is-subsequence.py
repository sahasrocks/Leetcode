class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # for c in t:
        #     if len(s)>0 and c ==s[0]:
        #         s=s[1:]
        # return len(s)==0        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)