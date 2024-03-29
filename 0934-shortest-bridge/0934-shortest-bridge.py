class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        island: List = []
        m: int = len(grid[0])
        n: int = len(grid)
        ans: int = -1

        def dfs(x: int, y: int,):
            if 0 <= x < m and 0 <= y < n and grid[y][x] == 1:
                island.append((x, y))
                grid[y][x] = 2
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        flag: bool = True
        for x in range(m):
            for y in range(n):
                if grid[y][x] == 1:
                    dfs(x, y)
                    flag = False
                    break
            if not flag:
                break

        while island:
            for _ in range(len(island)):
                x, y = island.pop(0)
                if 0 <= x < m and 0 <= y < n:
                    if grid[y][x] == 1:
                        return ans

                    if grid[y][x] != -1:
                        grid[y][x] = -1
                        island.append((x + 1, y))
                        island.append((x - 1, y))
                        island.append((x, y + 1))
                        island.append((x, y - 1))
            ans += 1
        
        return -1