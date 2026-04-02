class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols=len(mat),len(mat[0])
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=float('inf')
        while q:
            r,c=q.popleft()
            for dr,dc in dirs:
                row,col=r+dr,c+dc
                if 0<=row<rows and 0<=col<cols and mat[row][col]>mat[r][c]+1:
                    mat[row][col]=mat[r][c]+1
                    q.append((row,col))
        return mat                            


# class Solution:
# 	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
# 		row, col = len(mat), len(mat[0])
# 		queue = deque([])

# 		for x in range(row):
# 			for y in range(col):
# 				if mat[x][y] == 0:
# 					queue.append((x, y, 1))


# 		return self.bfs(row, col, queue, mat)

# 	def bfs(self, row, col, queue, grid):
# 		visited = set()
# 		while queue:
# 			x, y, steps = queue.popleft()

# 			for nx, ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
# 				if 0<=nx<row and 0<=ny<col and (nx,ny) not in visited:
# 					if grid[nx][ny] == 1:
# 						visited.add((nx,ny))
# 						grid[nx][ny] = steps
# 						queue.append((nx, ny, steps+1))

# 		return grid