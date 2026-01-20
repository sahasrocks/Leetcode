class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j,c=0,0,0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i+=1
                j+=1
                c+=1
            else:
                j+=1
        return c            
        
        
        # g.sort()
        # s.sort()
        # i=j=0
        # while i<len(g) and j<len(s):
        #     if g[i] <=s[j]:
        #         i+=1
        #     j+=1
        # return i        
        
        
        
        
        
        # g.sort(reverse=True)
        # s.sort(reverse=True)
        # i = j = 0
        # while i < len(g) and j < len(s):
        #     if g[i] <= s[j]:
        #         j += 1
        #     i += 1
        # return j