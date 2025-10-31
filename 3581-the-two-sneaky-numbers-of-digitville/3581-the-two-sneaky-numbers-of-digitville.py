class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # c=Counter(nums)
        # return [num for num,_ in c.most_common(2)]
        visited=set()
        res=[]
        for num in nums:
            if num in visited:
                res.append(num)
            else:
                visited.add(num)
        return res            

        