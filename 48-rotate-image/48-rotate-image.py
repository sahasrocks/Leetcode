class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
        """
        import numpy as np
        matrix[:] = np.rot90(matrix, axes=(1, 0))