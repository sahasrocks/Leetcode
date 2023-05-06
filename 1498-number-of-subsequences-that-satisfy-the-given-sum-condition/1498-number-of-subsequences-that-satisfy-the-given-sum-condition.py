class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        ans = 0
        lo, hi = 0, len(nums)-1
        while lo <= hi: 
            if nums[lo] + nums[hi] > target: hi -= 1
            else: 
                ans += pow(2, hi - lo, 1_000_000_007)
                lo += 1
        
        return ans % 1_000_000_007
