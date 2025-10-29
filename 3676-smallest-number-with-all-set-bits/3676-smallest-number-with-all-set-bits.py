class Solution:
    def smallestNumber(self, n: int) -> int:
        if n == 1:
            return 1
        for i in range(0, 11):
            if 2 ** i > n:
                return 2 ** i -1