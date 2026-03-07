class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=defaultdict(int)
        for i in s:
            c[i]+=1
        for i in range(len(s)):
            if c[s[i]]==1:
                return i
        return -1            
        
        
        # for i in range(len(s)):
        #     if s[i] not in s[:i] and s[i] not in s[i+1:]:
        #         return i
        # return -1        
        
        # for i in range(len(s)):
        #     if s[i] not in s[:i] and s[i] not in s[i+1::]:
        #         return i
        # return -1    
            

	         