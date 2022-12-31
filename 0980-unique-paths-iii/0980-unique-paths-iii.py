class Solution(object):
    def uniquePathsIII(self, grid):
        e, x, y = 0, 0, 0
        self.ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: x, y = i, j
                elif not grid[i][j]: e += 1
        
        def dfs(i, j, e):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == -1: return
            if grid[i][j] == 2:
                if not e: self.ans += 1
                return
            
            grid[i][j] = -1
            dfs(i + 1, j, e - 1)
            dfs(i - 1, j, e - 1)
            dfs(i, j + 1, e - 1)
            dfs(i, j - 1, e - 1)
            grid[i][j] = 0
        
        dfs(x, y, e + 1)
        return self.ans