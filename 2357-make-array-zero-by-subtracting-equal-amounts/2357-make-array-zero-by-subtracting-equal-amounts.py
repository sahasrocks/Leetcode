class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr=[i for i in nums if i>0]
        return len(set(arr))
            
        