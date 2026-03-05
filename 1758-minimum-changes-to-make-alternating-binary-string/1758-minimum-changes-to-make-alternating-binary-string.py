class Solution:
    def minOperations(self, s: str) -> int:
        c=0
        c1=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=='1':
                    c+=1
                if s[i]=='0':
                    c1+=1
            else:
                if s[i]=='0':
                    c+=1
                if s[i]=='1':
                    c1+=1
        return min(c,c1)                            