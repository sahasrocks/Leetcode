class Solution:
    def maxSubarraySum(self, nums, k):
        prefix = 0
        ans = float("-inf")

        # store MIN prefix sum for each mod class
        minPref = {i: float("inf") for i in range(k)}
        minPref[0] = 0  # prefix before starting the array

        for i, val in enumerate(nums):
            prefix += val
            mod = (i + 1) % k

            # valid subarray ending at i:
            ans = max(ans, prefix - minPref[mod])

            # update smallest prefix for this mod class
            minPref[mod] = min(minPref[mod], prefix)

        return ans

# from typing import List

# class Solution:
#     def maxSubarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         INF = 4 * 10**18
        
#         minPref = [INF] * k
        
#         prefix = 0
#         ans = -INF
        
#         minPref[0] = 0
        
#         for i, val in enumerate(nums):
#             prefix += val
#             rem = (i + 1) % k
            
#             if minPref[rem] != INF:
#                 ans = max(ans, prefix - minPref[rem])
            
#             if prefix < minPref[rem]:
#                 minPref[rem] = prefix
        
#         return ans