class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,v in enumerate(nums):
            rem=target-v
            if rem in a:
                return [a[rem],i]
            a[v]=i
        return []    