class Solution:
    def totalNQueens(self, n: int) -> int:
        res=0
        col=set()
        posD=set()
        negD=set()
        def backtrack(r):
            if r==n:
                nonlocal res
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in posD or (r-c) in negD:
                    continue
                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                backtrack(r+1)
                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
        backtrack(0)
        return res               

        
        
        
        
        
        
        
        
        
        
        
        
        # self.ans = 0
        
        # def place(i: int, vert: int, ldiag: int, rdiag:int) -> None:
        #     if i == N: self.ans += 1
        #     else:
        #         for j in range(N):
        #             vmask, lmask, rmask = 1 << j, 1 << (i+j), 1 << (N-i-1+j)
        #             if vert & vmask or ldiag & lmask or rdiag & rmask: continue
        #             place(i+1, vert | vmask, ldiag | lmask, rdiag | rmask)
            
        # place(0,0,0,0)
        # return self.ans