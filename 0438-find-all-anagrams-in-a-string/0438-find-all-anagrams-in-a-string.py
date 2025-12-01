class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        scount={}
        pcount={}
        if len(p)>len(s):
            return []
        for i in range(len(p)):
            pcount[p[i]]= 1+ pcount.get(p[i],0)
            scount[s[i]]=1+scount.get(s[i],0)

        res=[0] if pcount == scount else []
        l=0
        for r in range(len(p),len(s)):
            scount[s[r]] = 1 + scount.get(s[r],0)
            scount[s[l]] -= 1

            if scount[s[l]]==0:
                scount.pop(s[l])
            l+=1
            if scount==pcount:
                res.append(l)
        return res            




        # hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        # if pL > sL: return []

        # # build hashmap
        # for ch in p: hm[ch] += 1

        # # initial full pass over the window
        # for i in range(pL-1):
        #     if s[i] in hm: hm[s[i]] -= 1
            
        # # slide the window with stride 1
        # for i in range(-1, sL-pL+1):
        #     if i > -1 and s[i] in hm:
        #         hm[s[i]] += 1
        #     if i+pL < sL and s[i+pL] in hm: 
        #         hm[s[i+pL]] -= 1
                
        #     # check whether we encountered an anagram
        #     if all(v == 0 for v in hm.values()): 
        #         res.append(i+1)
                
        # return res