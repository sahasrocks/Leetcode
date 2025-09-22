class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=collections.Counter(nums)
        mx=max(c.values())
        count=0
        for v in c.values():
            if mx==v:
                count+=v
        return count         
        