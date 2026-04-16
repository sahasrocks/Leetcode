class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        left = [-1] * n
        mp = {}

        for i, num in enumerate(nums + nums):
            if i >= n:
                left[i - n] = i - mp[num] 
            mp[num] = i
        combos = nums + nums

        mp = {}
        right = [-1] * n
        for i in range(2*n-1, -1, -1):
            num = combos[i]
            if i < n:
                right[i] = mp[num] - i
            mp[num] = i

        res = []

        for i in queries:
            l = left[i]
            r = right[i]

            m = min(l, r)

            res.append(-1 if m >= n else m)

        return res