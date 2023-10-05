class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=[]
        n=len(nums)//3
        b=list(set(nums))
        for i in b:
            if nums.count(i)>n:
                a.append(i)
        return a        
        
        