class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        n = len(complexity)
        if n == 0:
            return 0
        root = complexity[0]
        for c in complexity[1:]:
            if c <= root:
                return 0
        res = 1
        for i in range(1, n):
            res = res * i % (10**9 + 7)
        return res