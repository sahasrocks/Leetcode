from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = 1

        for i in range(n):
            p = l = g = nums[i]
            for r in range(i + 1, n):
                x = nums[r]
                p *= x
                l = lcm(l, x)
                g = gcd(g, x)
                if p == l * g:
                    ans = max(ans, r - i + 1)
        return ans
