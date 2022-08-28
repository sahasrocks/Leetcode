class Solution(object):
    def diagonalSort(self, M):
        y, x = len(M), len(M[0])
        for i in range(2-y, x-1):
            valid = range(max(0,0-i), min(y,x-i))
            diag = sorted([M[j][i+j] for j in valid])
            for k in valid:
                M[k][i+k] = diag.pop(0)
        return M