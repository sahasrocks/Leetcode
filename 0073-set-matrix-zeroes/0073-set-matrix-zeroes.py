class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowHasZero = not all(matrix[0])
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if firstRowHasZero:
            matrix[0] = [0]*len(matrix[0])