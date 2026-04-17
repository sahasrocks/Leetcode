class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            res = 0
            while x:
                res *= 10
                res += x % 10
                x = x // 10
            return res
        
        prev = {}
        ans = inf
        for i, num in enumerate(nums):
            if num in prev: #there is a prev match.
                ans = min(ans, i - prev[num])
            
            prev[reverse(num)] = i #or int(str(num)[::-1]) to get reverse.
        
        return ans if ans != inf else -1