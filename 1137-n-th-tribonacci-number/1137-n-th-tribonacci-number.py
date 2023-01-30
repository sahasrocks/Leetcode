class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0:
            return 0
        for i in range(n-2):
            a, b, c = b, c, (a+b+c)
        return c