class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q=deque([(0,0,1)])
        visited=set((0,0))
        dirs=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        while q:
            r,c,length=q.popleft()
            if r==n-1 and c==n-1:
                return length
            for dr,dc in dirs:
                nr,nc=dr+r,dc+c
                if (nr in range(n) and nc in range(n) and (nr,nc) not in visited and grid[nr][nc]==0):
                    q.append((nr,nc,length+1))
                    visited.add((nr,nc))
        return -1                

        
        # n= len (grid)
        # if grid[0][0] or grid[n-1][n-1]:
        #     return -1
        # q=deque([(0,0,1)])
        # visited=set((0,0))
        # dirs=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        # while q:
        #     r,c,length=q.popleft()
        #     if r==n-1 and c==n-1:
        #         return length
        #     for dr,dc in dirs:
        #         nr,nc=r+dr,c+dc
        #         if ( 0<=nr<n and 0<=nc<n  and grid[nr][nc] ==0 and (nr,nc) not in visited ):
        #             q.append((nr,nc,length+1))
        #             visited.add((nr,nc))
        # return -1               