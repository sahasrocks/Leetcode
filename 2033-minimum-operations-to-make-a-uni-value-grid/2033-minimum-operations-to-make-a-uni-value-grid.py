class Solution:
    def minOperations(self, grid, x):
        m, n = len(grid), len(grid[0])
        arr = []
        rem = grid[0][0] % x

        for row in grid:
            for num in row:
                if num % x != rem:
                    return -1
                arr.append(num)

        arr.sort()
        median = arr[len(arr) // 2]
        return sum(abs(num - median) // x for num in arr)