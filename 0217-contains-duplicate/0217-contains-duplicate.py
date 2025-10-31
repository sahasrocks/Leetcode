class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited=set()
        for i in nums:
            if i not in visited:
                visited.add(i)
        if len(nums) == len(visited):
            return False
        else:
            return True            
        
        
        
        
        
        
        
        
        
        # a=len(nums)
        # b=len(set(nums))
        # return a!=b        