class Solution:
    def search(self, nums: List[int], t: int) -> int:
        low = 0
        high = len(nums)-1
        mid=0
        while low<=high:
            mid = (high+low)//2
            if nums[mid]<t:
                low = mid+1
            elif nums[mid]>t:
                high = mid-1
            else:
                return mid
        return -1    