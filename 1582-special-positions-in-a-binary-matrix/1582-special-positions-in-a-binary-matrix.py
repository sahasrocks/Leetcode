class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        c=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and sum(mat[i])==1 and sum(row[j] for row in mat)==1:
                    c+=1
        return c            