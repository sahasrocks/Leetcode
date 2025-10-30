class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap=[]
        for num in nums:
            if len(min_heap)<k:
                heapq.heappush(min_heap,int(num))
            else:
                heapq.heappushpop(min_heap,int(num))
        return str(min_heap[0])            
        