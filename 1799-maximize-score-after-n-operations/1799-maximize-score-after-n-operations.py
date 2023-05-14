from collections import defaultdict 
import math
class Solution:
    def maxScore(self, nums: List[int]) -> int:

        D=defaultdict(int)

        n=len(nums)
        bit=0
        for i in range(n):
            bit+=(2**i)
        
        #visited=set()
        def sol(bit,count):
            if not bit:
                return 0
            if D[bit]:
                return D[bit]
            maxx=0
            for i in range(n):
                if bit & 1<<i:
                    for j in range(i+1,n):
                        if bit & 1<<j:
                            local=bit
                            local=local^(1<<i)
                            local=local^(1<<j)
                            y=count*(math.gcd(nums[i],nums[j]))+sol(local,count+1)
                            maxx=max(maxx,y)
            #visited.add(bit)
            D[bit]=maxx
            return maxx
        
        return sol(bit,1)