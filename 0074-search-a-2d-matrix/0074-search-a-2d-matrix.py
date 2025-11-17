class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        t=m*n
        l=0
        r=t-1
        while l<=r:
            m=(l+r)//2
            i=m//n
            j=m%n
            mid_num=matrix[i][j]
            if target==mid_num:
                return True
            elif target<mid_num:
                r=m-1
            else:
                l=m+1
        return False                
        
        
        
        
        
        
        
        
        
        # ROWS, COLS = len(matrix), len(matrix[0])

        # top, bot = 0, ROWS - 1
        # while top <= bot:
        #     row = (top + bot) // 2
        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bot = row - 1
        #     else:
        #         break

        # if not (top <= bot):
        #     return False
        # row = (top + bot) // 2
        # l, r = 0, COLS - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if target > matrix[row][m]:
        #         l = m + 1
        #     elif target < matrix[row][m]:
        #         r = m - 1
        #     else:
        #         return True
        # return False
        
        
        
        
        # ROWS, COLS = len(matrix), len(matrix[0])

        # l, r = 0, ROWS * COLS - 1
        # while l <= r:
        #     m = l + (r - l) // 2
        #     row, col = m // COLS, m % COLS
        #     if target > matrix[row][col]:
        #         l = m + 1
        #     elif target < matrix[row][col]:
        #         r = m - 1
        #     else:
        #         return True
        # return False          