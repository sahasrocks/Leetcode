class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        summ = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        lon = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                summ[i][j] = summ[i-1][j]+summ[i][j-1]-summ[i-1][j-1]+mat[i-1][j-1]
                if i>= lon and j>=lon and summ[i][j]-summ[i-lon][j] - summ[i][j-lon]+summ[i-lon][j-lon]<=threshold:
                    res = lon
                    lon+=1
        return res