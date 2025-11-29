class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a=sum(nums)
        b=0
        if a%k==0:
            return 0
        while a%k !=0:
            a-=1
            b+=1
        return b    

        