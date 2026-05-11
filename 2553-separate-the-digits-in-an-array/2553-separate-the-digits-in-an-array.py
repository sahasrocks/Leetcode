class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            s=str(i)
            for ch in s:
                res.append(int(ch))
        return res        