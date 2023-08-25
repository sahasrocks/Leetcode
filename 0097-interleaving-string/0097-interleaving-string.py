class Solution:
    @lru_cache
    def helper(self, s1, s2, s3, i1, i2, i3):
        if i3 < 0:
            return True
        if i3 + 1 != i1 + i2 + 2:
            return False
        if i1 >= 0 and i2 >= 0 and s1[i1] == s3[i3] and s2[i2] == s3[i3]:
            return self.helper(s1, s2, s3, i1 - 1, i2, i3 - 1) or \
                   self.helper(s1, s2, s3, i1, i2 - 1, i3 - 1)
        elif i1 >= 0 and s1[i1] == s3[i3]:
            return self.helper(s1, s2, s3, i1 - 1, i2, i3 - 1)
        elif i2 >= 0 and s2[i2] == s3[i3]:
            return self.helper(s1, s2, s3, i1, i2 - 1, i3 - 1)
        return False
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        return self.helper(s1, s2, s3, len(s1) - 1, len(s2) - 1, len(s3) - 1)