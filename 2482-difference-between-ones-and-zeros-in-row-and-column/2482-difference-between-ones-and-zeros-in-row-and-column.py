class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        lis = [ [0]*len(grid[0]) for i in range(len(grid))]
        # grid1 = [ [0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] =-1
        
                
        
        
        rows = {}
        cols = {}
        ele = 0
        for i in range(len(grid)):
            rows[i] = sum(grid[i])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j not in cols:
                    cols[j] = grid[i][j] 
                else:
                    cols[j] += grid[i][j] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ele = rows[i]+cols[j]
                lis[i][j] = ele
            
        return lis
        