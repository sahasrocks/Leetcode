class Solution(object):
    def partition(self, s):
        res=[]
        part=[]
        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.ispali(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

    def ispali(self,s,l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            l,r=l+1,r-1
        return True                            
        
        
        
        
        # res=[]
        # def pallindrome(a):
        #     return a==a[::-1]
        # def dfs(i,cur):
        #     if i==len(s):
        #         res.append(cur)
        #         return
        #     for j in range(i,len(s)):
        #         sol=s[i:j+1]
        #         if pallindrome(sol):
        #             dfs(j+1,cur+[sol])
        #     return
        # dfs(0,[])
        # return res                    