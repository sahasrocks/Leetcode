class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-1
        while r-l>=k:
            if abs(x-arr[l])<=abs(arr[r]-x):
                r-=1
            else:
                l+=1
        return arr[l:r+1]            
        
        # beg = k
        # end = len(arr)
        # while beg < end:
        #     mid = (beg+end) // 2
        #     a = arr[mid]
        #     b = arr[mid-k]
        #     if (a-x) >= (x-b):
        #         end = mid
        #     else:
        #         beg = mid + 1
        # return arr[beg-k:end]