class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i,e in enumerate(nums):
            diff=target-e
            if diff in m:
                return [m[diff],i]
            m[e]=i

        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
       
       
       
        # m={}
        # for i,e in enumerate(nums):
        #     diff=target-e
        #     if diff in m:
        #         return [m[diff],i]
        #     m[e]=i    
        
        
        # m={}
        # for i,e in enumerate(nums):
        #     diff=target-e
        #     if diff in m:
        #         return [m[diff],i]
        #     m[e]=i    


        # m={}
        # for i,e in enumerate(nums):
        #     diff=target-e
        #     if diff in m:
        #         return [m[diff],i]
        #     m[e]=i
                
        
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