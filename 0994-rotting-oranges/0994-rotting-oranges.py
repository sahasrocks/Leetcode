class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        m,n=len(grid),len(grid[0])
        fresh,time=0,0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        while fresh>0 and q:
            length=len(q)
            for i in range(length):
                r,c=q.popleft()
                for dr,dc in dirs:
                    rows,cols=r+dr,c+dc
                    if (rows in range(m) and cols in range(n) and grid[rows][cols]==1):
                        grid[rows][cols]=2
                        q.append((rows,cols))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # q=deque()
        # fresh=0
        # m,n=len(grid),len(grid[0])
        # time=0
        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c]==1:
        #             fresh+=1
        #         if grid[r][c]==2:
        #             q.append((r,c))
        # dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        # while fresh>0 and q:
        #     length=len(q)
        #     for i in range(length):
        #         r,c = q.popleft()
        #         for dr,dc in dirs:
        #             row,col=dr+r,dc+c
        #             if (row in range(m) and col in range(n) and grid[row][col]==1):
        #                 grid[row][col]=2
        #                 q.append((row,col))
        #                 fresh-=1
        #     time+=1
        # return time if fresh==0 else -1                            

        
        
        
        
        
        
        
        
        # q=deque()
        # fresh=0
        # m,n=len(grid),len(grid[0])
        # time=0
        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c] ==1:
        #             fresh+=1
        #         if grid[r][c]==2:
        #             q.append((r,c))
        # dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        # while fresh>0 and q:
        #     length=len(q)
        #     for i in range(length):
        #         r,c=q.popleft()
        #         for dr,dc in dirs:
        #             row,col=r+dr,c+dc
        #             if (row in range(m) and col in range(n) and grid[row][col]==1):
        #                 grid[row][col]=2
        #                 q.append((row,col))
        #                 fresh-=1
        #     time+=1
        # return time if fresh==0 else -1                


        
        # q=deque()
        # fresh=0
        # time=0
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 1:
        #             fresh+=1
        #         if grid[r][c] == 2:
        #             q.append((r,c))
        # dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        # while fresh > 0 and q:
        #     lenght=len(q)
        #     for i in range(lenght):
        #         r,c=q.popleft()
        #         for dr,dc in dirs:
        #             row,col=r+dr,c+dc
        #             if ( row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1 ) :
        #                 grid[row][col]=2
        #                 q.append((row,col))
        #                 fresh-=1
        #     time+=1
        # return time if fresh==0 else -1                               