class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m ,n = len(grid),len(grid[0])
        top = 0
        left = 0
        bottom = m-1
        right = n-1
        while top<bottom and left<right:
            layer = []
            for i in range(left,right+1):
                layer.append(grid[top][i])
            for i in range(top+1,bottom+1):
                layer.append(grid[i][right])
            for i in range(right-1,left-1,-1):
                layer.append(grid[bottom][i])
            for i in range(bottom-1,top,-1):
                layer.append(grid[i][left])
            
            
            k_mod = k%len(layer)
            rotated_layer = layer[k_mod:]+layer[:k_mod]

            idx=0
            for i in range(left,right+1):
                grid[top][i]=rotated_layer[idx]
                idx+=1

            for i in range(top+1,bottom+1):
                grid[i][right]=rotated_layer[idx]
                idx+=1
            for i in range(right-1,left-1,-1):
                grid[bottom][i]=rotated_layer[idx]
                idx+=1
            for i in range(bottom-1,top,-1):
                grid[i][left]=rotated_layer[idx]
                idx+=1
            
            top+=1
            left+=1
            right-=1
            bottom-=1
        return grid