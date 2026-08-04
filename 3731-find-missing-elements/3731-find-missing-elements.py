class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m = min(nums)
        n = max(nums)
        s = []
        for i in range(m,n+1):
            if i not in nums:
                s.append(i)
        return s