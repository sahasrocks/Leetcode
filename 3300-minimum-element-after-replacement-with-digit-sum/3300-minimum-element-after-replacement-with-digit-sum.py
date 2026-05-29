class Solution:
    def minElement(self, nums: List[int]) -> int:
        l=[]
        for num in nums:
            n=str(num)
            s=0
            for ch in n:
                s+=int(ch)
            l.append(s)
        return min(l)