class Solution:
    def largestVariance(self, s: str) -> int:
        # Find max subarray sum if at least one -1 is included. 
        # dp[i] the max subarray with at least one -1 sum that ends at i
        # dp[i + 1] = if nums[i + 1] == 1, dp[i] + 1
        #             if nums[i + 1] == -1, dp[i] - 1
        #.                   if dp[i] > 0 dp[i] (the start index nums[start] == -1, we move start one step forward) or dp[i] - 1
        #.                   if dp[i] <= 0 start = i, 0
        def kadane(nums):
            n = len(nums)
            dp = nums[0]
            start = 0
            valid = nums[0] == -1 # if a -1 is included, the result is valid.
            max_dp = 0
            for i in range(1, n):
                next_dp = 0
                if nums[i] == 1:
                    next_dp = dp + 1
                else:# nums[i] == -1:
                    if not valid:
                        next_dp = dp - 1
                        valid = True
                    else:
                        if dp >= 0:
                            if nums[start] == -1:
                                next_dp = dp
                                start += 1
                            else:
                                if dp == 0:
                                    next_dp = -1
                                    start = i
                                else:
                                    next_dp = dp - 1
                        else:
                            start = i
                            next_dp = -1
                dp = next_dp
                if valid:
                    max_dp = max(dp, max_dp)
            return max_dp
        n = len(s)
        letters = set(s)
        if len(letters) == 1:
            return 0
        ans = -float('inf')
        for a in letters:
            for b in letters:
                if a == b:
                    continue
                nums = list(map(lambda ch: 1 if ch == a else -1, filter(lambda ch: ch == a or ch == b, s)))
                res = kadane(nums)
                ans = max(ans, res)
        return ans