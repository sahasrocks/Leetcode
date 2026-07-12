class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(set(arr))
        nums = {y : x for x, y in enumerate(nums)}
        
        return [nums[n] + 1 for n in arr]
        