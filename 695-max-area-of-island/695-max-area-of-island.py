class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def scan(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + sum(starmap(scan, [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]))
            return 0
        return max( scan(i, j) for i in range(m) for j in range(n))