class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while nums:
            if original in nums:
                original *=2
                continue
            break
        return original        
        