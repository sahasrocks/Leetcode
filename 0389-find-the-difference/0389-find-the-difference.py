class Solution(object):
    def findTheDifference(self, s, t):
        S=list(s)
        S.sort()
        T=list(t)
        T.sort()
        for i in range(len(S)):
            if T[i]!=S[i]:
                return T[i]            
        return T[-1]