class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q=deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if ( (r in range(rows)) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit ):
                        q.append((r,c))
                        visit.add((r,c))
        if not grid:
            return 0
        rows=len(grid)  
        cols=len(grid[0])
        visit=set()
        island=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island                         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not grid or not grid[0]:
        #     return 0
        
        # islands = 0
        # visit = set()
        # rows, cols = len(grid), len(grid[0])
        
        # def dfs(r, c):
        #     if (r not in range(rows) or
        #         c not in range(cols) or
        #         grid[r][c] == "0" or
        #         (r, c) in visit):
        #         return
            
        #     visit.add((r, c))
        #     directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visit:
        #             islands += 1
        #             dfs(r, c)
        # return islands
                                                                    