class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i,e in enumerate(nums):
            diff=target-e
            if diff in m:
                return [m[diff],i]
            m[e]=i
                
        
        # m={}
        # for i,n in enumerate(nums):
        #     diff=target-n
        #     if diff in m:
        #         return [m[diff],i]
        #     m[n]=i    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # m= {}
        # for i,n in enumerate(nums):
        #     diff = target - n
        #     if diff in m:
        #         return [m[diff],i]
        #     m[n] = i      