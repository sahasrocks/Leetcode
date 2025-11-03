class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i,v in enumerate(numbers):
        #     diff= target - v
        #     if diff in numbers:
        #         return (i+1, numbers.index(diff)+1)
        # l,r=0,len(numbers)-1
        # while l<r:
        #     s=numbers[l]+numbers[r]
        #     if s==target:
        #         return [l+1,r+1]
        #     elif s<target:
        #         l+=1
        #     else:
        #         r-=1








        l=0
        r=len(numbers)-1
        while l<r:
            s=numbers[l]+numbers[r]
            if s==target:
                return [l+1,r+1]
            elif s<target:
                l+=1
            else:
                r-=1        

