class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        totalSum = 0
        for idx in range(M):
            for jdx in range(N):
                totalSum += grid[idx][jdx]
        
        # Sweep down
        topSum = 0
        bottomSum = totalSum
        for idx in range(M-1):
            curRow = 0
            for jdx in range(N):
                curRow += grid[idx][jdx]
        
            topSum += curRow
            bottomSum -= curRow
            if topSum == bottomSum:
                return True

        # Sweep right
        leftSum = 0
        rightSum = totalSum
        for jdx in range(N-1):
            curCol = 0
            for idx in range(M):
                curCol += grid[idx][jdx]

            leftSum += curCol
            rightSum -= curCol
            if leftSum == rightSum:
                return True

        return False       