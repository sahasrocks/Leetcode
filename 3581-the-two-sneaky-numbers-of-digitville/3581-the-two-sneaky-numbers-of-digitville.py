class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        return [num for num,_ in c.most_common(2)]

        