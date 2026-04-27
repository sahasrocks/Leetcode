class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions: (dy, dx) → Up, Down, Left, Right
        dirs = {
            1: [(0, -1), (0, 1)],       # Left, Right
            2: [(-1, 0), (1, 0)],       # Up, Down
            3: [(0, -1), (1, 0)],       # Left, Down
            4: [(0, 1), (1, 0)],        # Right, Down
            5: [(0, -1), (-1, 0)],      # Left, Up
            6: [(0, 1), (-1, 0)]        # Right, Up
        }

        # Reverse direction match for bi-directional check
        opposites = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (1, 0): (-1, 0),
            (-1, 0): (1, 0)
        }
        
        visited = [[False]*n for _ in range(m)]
        
        def dfs(r, c):
            if r == m-1 and c == n-1:
                return True
            visited[r][c] = True
            for dy, dx in dirs[grid[r][c]]:
                nr, nc = r + dy, c + dx
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if opposites[(dy, dx)] in dirs[grid[nr][nc]]:
                        if dfs(nr, nc):
                            return True
            return False
        
        return dfs(0, 0)