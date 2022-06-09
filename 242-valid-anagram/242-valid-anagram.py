class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(s)
        l2=list(t)
        l1.sort()
        l2.sort()
        
        position = 0
        matches = True
        if len(s)<len(t) or len(t)<len(s):
            matches = False
        while position < len(s) and matches:
            if l1[position] ==l2[position]:
                position = position +1
            else:
                matches = False
        return matches    