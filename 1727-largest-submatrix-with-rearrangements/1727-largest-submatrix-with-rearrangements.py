class Solution:
    def largestSubmatrix(self,matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        max_area = 0

        for i in range(1,rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        for val in matrix:
            val.sort(reverse=True)
        
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                max_area = max(max_area, matrix[i][j] * (j + 1))
        
        return max_area