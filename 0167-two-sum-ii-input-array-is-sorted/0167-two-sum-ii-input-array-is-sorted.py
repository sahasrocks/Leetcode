class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,n=0,len(nums)-1
        while i< n:
            cs= nums[i]+nums[n]
            if cs>target:
                n-=1
            elif cs<target:
                i+=1
            else:
                return [i+1,n+1]    
            
        #prevMap = {}  # val -> index

        #for i, n in enumerate(nums):
            #diff = target - n
            #if diff in prevMap:
            #    return [prevMap[diff]+1, i+1]
            #prevMap[n] = i
             
        