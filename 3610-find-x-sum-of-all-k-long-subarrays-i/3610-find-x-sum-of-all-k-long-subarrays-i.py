from collections import Counter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freqs = Counter(sub)
            ordered = sorted(freqs.items(), key=lambda p: (-p[1], -p[0]))
            toKeep = {v for v, _ in ordered[:x]}
            res.append(sum(val for val in sub if val in toKeep))
        return res