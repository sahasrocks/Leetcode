class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=defaultdict(int)
        l,res=0,0
        for r in range(len(s)):
            c[s[r]]+=1
            while r-l+1 -max(c.values())>k:
                c[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res        












        
               
        # c=defaultdict(int)
        # l,res=0,0
        # for r in range(len(s)):
        #     c[s[r]]+=1
        #     while (r-l+1)-max(c.values())>k:
        #         c[s[l]]-=1
        #         l+=1
        #     res=max(res,r-l+1)
        # return res        
        
        
        # c=defaultdict(int)
        # l=0
        # res=0
        # for r in range(len(s)):
        #     c[s[r]]+=1
        #     while (r-l+1) - max(c.values())>k:
        #         c[s[l]]-=1
        #         l+=1
        #     res=max(res,r-l+1)
        # return res        
        
        # count=defaultdict(int)
        # l=0
        # res=0
        # for r in range(len(s)):
        #     count[s[r]]+=1
        #     while (r-l+1) - max(count.values()) >k:
        #         count[s[l]]-=1
        #         l+=1
        #     res=max(res,r-l+1)
        # return res        

        # count=defaultdict(int)
        # l=0
        # res=0
        # for r in range(len(s)):
        #     count[s[r]]+=1
        #     while (r-l+1) - max(count.values())>k:
        #         count[s[l]]-=1
        #         l+=1
        #     res=max(res,r-l+1)
        # return res        

        
        
        # count={}
        # l=0
        # res=0
        # for r in range(len(s)):
        #     count[s[r]]=1+count.get(s[r],0)
        #     while (r-l+1) - max(count.values())>k:
        #         count[s[l]]-=1
        #         l+=1
        #     res=max(res,r-l+1)
        # return res        