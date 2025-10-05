class Solution:
    def pacificAtlantic(self, grid):
        
        m,n=len(grid),len(grid[0])
        vis1,vis2=[[0 for _ in range(n)]for _ in range(m)],[[False for _ in range(n)]for _ in range(m)]
        
        def isValid(x,y,vis):
            if x<0 or x>m-1 or y<0 or y>n-1:
                return False
            if vis[x][y]:
                return False
            return True
        
        def dfs(x,y,vis):
            vis[x][y]=True
            for cx,cy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if isValid(cx,cy,vis) and grid[cx][cy]>=grid[x][y]:
                    dfs(cx,cy,vis)

        for i in range(m):
            dfs(i,0,vis1)
        for j in range(n):
            dfs(0,j,vis1)
        
        
        for i in range(m):
            dfs(i,n-1,vis2)
        for j in range(n):
            dfs(m-1,j,vis2)
        
        
        res=[]
        for x in range(m):
            for y in range(n):
                if vis1[x][y] and vis2[x][y]:
                    res.append([x,y])
        return res   
        