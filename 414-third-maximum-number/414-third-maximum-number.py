class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        l.sort()
        return l[-3] if len(l)>=3 else l[-1]