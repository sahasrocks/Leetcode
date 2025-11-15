class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0

        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[r]==s[l]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[r]==s[l]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1  
        return res              
        
        
        
        
        
        
        
        
        
        # temp = ''
        # maxp = ''

        # for i in range(len(s)):
        #     temp += s[i]
        #     for j in range(len(temp)):
        #         if temp[j] == s[i] and s[j:i+1] == s[j:i+1][::-1] and len(s[j:i+1]) > len(maxp):
        #             maxp = s[j:i+1]
        #             break

        # return maxp                