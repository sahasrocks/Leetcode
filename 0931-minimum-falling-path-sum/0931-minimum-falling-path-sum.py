class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        prev=[0]*m
        for i in range(m):
            prev[i]=matrix[0][i]
        for i in range(1,n):
            curr=[0]*m
            for j in range(m):
                up=prev[j]+matrix[i][j]
                if j-1>=0:
                    left=prev[j-1]+matrix[i][j]
                else:
                    left=1e9+matrix[i][j]

                if j+1<m:
                    right=prev[j+1]+matrix[i][j]
                else:
                    right=1e9+matrix[i][j]
                curr[j]=min(up,left,right)
            prev=curr
        return min(prev)