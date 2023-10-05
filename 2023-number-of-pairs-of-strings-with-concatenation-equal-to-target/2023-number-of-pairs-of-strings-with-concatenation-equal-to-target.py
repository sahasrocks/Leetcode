class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        a=0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if str(nums[i])+str(nums[j])==str(target) :
                        a+=1
        return a        
        