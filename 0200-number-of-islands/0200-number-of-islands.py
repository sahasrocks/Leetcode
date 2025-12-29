class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if (i<0 or i>=m or j<0 or j>=n or grid[i][j] !='1'):
                return 
            else:
                grid[i][j]='0'
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)
        num_i=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] =='1':
                    num_i+=1
                    dfs(i,j)
        return num_i                        



        # def bfs(r,c):
        #     q=deque()
        #     visit.add((r,c))
        #     q.append((r,c))
        #     while q:
        #         row,col=q.popleft()
        #         directions=[[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr,dc in directions:
        #             r,c=row+dr,col+dc
        #             if ( (r in range(rows)) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit ):
        #                 q.append((r,c))
        #                 visit.add((r,c))
        # if not grid:
        #     return 0
        # rows=len(grid)  
        # cols=len(grid[0])
        # visit=set()
        # island=0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c]=="1" and (r,c) not in visit:
        #             bfs(r,c)
        #             island+=1
        # return island                         
        

        # def dfs(r,c):
        #     if ( r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0" or (r,c) in visit ):
        #         return
        #     visit.add((r,c))
        #     dfs(r + 1, c)  # down
        #     dfs(r - 1, c)  # up
        #     dfs(r, c + 1)  # right
        #     dfs(r, c - 1)  # left
        # if not grid:
        #     return 
        # rows, cols = len(grid), len(grid[0])
        # visit = set() 
        # island=0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c]=="1" and (r,c) not in visit:
        #             dfs(r,c)
        #             island+=1
        # return island            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
                                                                    