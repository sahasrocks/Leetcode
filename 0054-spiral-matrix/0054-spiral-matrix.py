class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m,n=len(matrix),len(matrix[0])
        top,bot,l,r=0,m-1,0,n-1
        while len(res)<m*n:
            for i in range(l,r+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bot+1):
                res.append(matrix[i][r])
            r-=1
            if top<=bot:
                for i in range(r,l-1,-1):
                    res.append(matrix[bot][i])
                bot-=1
            if l<=r:
                for i in range(bot,top-1,-1):
                    res.append(matrix[i][l])
                l+=1
        return res                    


        
        # res = []
        # if not matrix:
        #     return []
        # i,j,di,dj = 0,0,0,1
        # m, n = len(matrix),len(matrix[0])
        # for v in range(m * n):
        #     res.append(matrix[i][j])
        #     matrix[i][j] = ''
        #     if matrix[(i+di)%m][(j+dj)%n] == '':
        #         di, dj = dj, -di
        #     i += di
        #     j += dj
        # return res