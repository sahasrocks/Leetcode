class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT,window={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)

        have,need=0,len(countT)
        res,resLen=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            if c in countT and window[c]==countT[c]:
                have+=1

            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                window[s[l]]-=1
                if s[l] in  countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen != float("infinity") else ""              

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # need, missing = collections.Counter(t), len(t)
        # i = I = J = 0
        # for j, c in enumerate(s, 1):
        #     missing -= need[c] > 0
        #     need[c] -= 1
        #     if not missing:
        #         while i < j and need[s[i]] < 0:
        #             need[s[i]] += 1
        #             i += 1
        #         if not J or j - i <= J - I:
        #             I, J = i, j
        # return s[I:J]