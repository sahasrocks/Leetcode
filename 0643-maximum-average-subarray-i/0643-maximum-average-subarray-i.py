class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxS=curS=sum(nums[:k])
        for i in range(k,len(nums)):
            curS += nums[i] - nums[i-k]
            maxS=max(maxS,curS)
        return maxS/k    
        