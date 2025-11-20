class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in cs:
                cs.remove(s[l])
                l+=1
            cs.add(s[r])
            res=max(res,r-l+1)
        return res         
        
        # res=0
        # for i in range(len(s)):
        #     cs=set()
        #     for j in range(i,len(s)):
        #         if s[j] in cs:
        #             break
        #         cs.add(s[j])
        #     res=max(res,len(cs))
        # return res    

        
        
        
        
        
        
        
        # l=0
        # res=0
        # charSet=set()
        # for i in range(len(s)):
        #     while s[i] in charSet:
        #         charSet.remove(s[l])
        #         l+=1
        #     charSet.add(s[i])
        #     res=max(res,i-l+1)
        # return res        
        
        
        
        
        
        
        
        
        
        
        
        # l=0
        # res=0
        # charset=set()
        # for i in range(len(s)):
        #     while s[i] in charset:
        #         charset.remove(s[l])
        #         l+=1
        #     charset.add(s[i])
        #     res=max(res,i-l+1)
        # return res        
        