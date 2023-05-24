class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums=[]
        for x,y in zip(nums1,nums2):
            nums.append((x,y))
            
        nums.sort(key=lambda x:-x[1])
        h=[]
        best=0
        total=0
        for x,y in nums:
            heapq.heappush(h,x)
            total+=x
            if len(h)>k:
                t=heapq.heappop(h)
                total-=t
            if len(h)==k:
                
                best=max(best,total*y)
                
        return best         