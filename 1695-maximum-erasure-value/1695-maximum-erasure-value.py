class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq, l, cur_sum, ans  = [False]*10001, 0, 0, 0
        for r in range(len(nums)):
            while freq[nums[r]]:
                freq[nums[l]] = False
                cur_sum -= nums[l]
                l += 1
            freq[nums[r]] = True
            cur_sum += nums[r]
            ans = max(ans, cur_sum)
        return ans