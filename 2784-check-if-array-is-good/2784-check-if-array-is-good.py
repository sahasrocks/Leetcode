class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)

        # 1. sort increasingly
        nums = sorted(nums)
       
        # 2. check greedily
        for i in range(n - 1):
            # stop
            if nums[i] != i + 1:
                return False
        
        # 3. check last cell
        return nums[n - 1] == n - 1