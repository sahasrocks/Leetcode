class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l = len(nums)
        n = sum(nums)-l*nums[0]
        a = [n]
        for i in range(l-1):
            n -= (nums[i+1]-nums[i])*(-i+l-2-i)
            a.append(n)
        return a
        