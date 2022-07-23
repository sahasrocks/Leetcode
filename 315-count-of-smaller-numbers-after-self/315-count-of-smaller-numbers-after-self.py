from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # a=[]
        # c=0
        # for i in range(len(nums)):
        #     for k in range(i+1,len(nums)):
        #         if nums[i]>nums[k]:
        #             c+=1
        #     a.append(c)
        #     c=0
        # return  a        
        n = len(nums)
        smaller = [-1] * n
        tempNums = SortedList()
        for key, num in enumerate(nums[::-1]):
            smaller[n - key - 1] = tempNums.bisect_left(num)
            tempNums.add(num)
        return smaller