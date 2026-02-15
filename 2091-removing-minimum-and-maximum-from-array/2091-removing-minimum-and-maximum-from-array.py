class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        maxi, mini = float(-inf), float(inf)
        ind_max, ind_min = -1, -1
        for i, num in enumerate(nums):
            if num > maxi:
                ind_max = i
                maxi = num
            if num < mini:
                ind_min = i
                mini = num
        
        x, y = ind_max, ind_min
        if x > y:
            x, y = y, x
        
        return min([y + 1, n - x, x + 1 + n - y])