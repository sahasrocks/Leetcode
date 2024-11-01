class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        t=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            low = i+1
            high = len(nums)-1
            while low < high:
                cs= nums[i] + nums[low] +nums[high]
                if cs<0:
                    low+=1
                elif cs>0:
                    high-=1
                else:
                    t.append([nums[i],nums[low],nums[high]])

                    while low<high and nums[low]==nums[low+1]:
                        low+=1
                    low+=1
                    high-=1
        return t                        
        