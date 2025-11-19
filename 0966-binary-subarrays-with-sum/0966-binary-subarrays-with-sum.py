class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=0
        ps=0
        preSum=defaultdict(int)
        preSum[0]=1
        for n in nums:
            ps+=n
            diff=ps-goal
            res+=preSum[diff]
            preSum[ps]+=1
        return res    

        