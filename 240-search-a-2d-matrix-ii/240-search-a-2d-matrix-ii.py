class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        # we initialize the pointer at the bottom-left of the matrix
        r,c = len(matrix)-1,0
        while r >=0 and c <len(matrix[0]):
            if matrix[r][c] == target:
                return True
            else:
                if matrix[r][c] < target:
                    c += 1
                else:
                    r -= 1
        return False