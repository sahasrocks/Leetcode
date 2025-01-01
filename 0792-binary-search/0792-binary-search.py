#   class Solution:
#     def search(self, num: List[int], target: int) -> int:
#         l=0
#         h=len(num)-1
        
#         while l<=h:
#             m= l + ((h-1)//2)
#             if num[m] > target:
#                 h=m-1
#             elif num[m] < target:
#                 l=m+1
#             else:
#                 return m
#         return -1    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)  

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1          
            
        