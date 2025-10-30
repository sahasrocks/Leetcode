class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        l1=1
        for i in range(n):
            g=l=p=nums[i]
            for r in range(i+1,n):
                x=nums[r]
                p*=x
                l=lcm(l,x)
                g=gcd(g,x)
                if p==l*g:
                    l1=max(l1,r-i+1)
        return l1            