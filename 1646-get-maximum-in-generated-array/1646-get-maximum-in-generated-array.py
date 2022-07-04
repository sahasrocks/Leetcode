class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:
            return n

        nums = [0] * (n + 1)
        nums[1] = 1

        for i in range(2, n + 1):           
            if i % 2:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]

            else:
                nums[i] = nums[i // 2]

        return max(nums)