class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0]*(2*limit+2)
        for i in range(n//2):
            a,b = nums[i],nums[n-1-i]
            x,y = min(a,b),max(a,b)
            diff[x+1]-=1
            diff[y+limit+1]+=1
            diff[a+b]-=1
            diff[a+b+1]+=1
        cur = n
        minMoves = float('inf')
        for s in diff:
            cur+=s
            minMoves = min(minMoves,cur)
        return minMoves

