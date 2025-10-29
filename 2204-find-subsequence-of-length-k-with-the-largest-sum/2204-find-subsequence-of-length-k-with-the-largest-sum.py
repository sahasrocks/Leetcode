# class Solution:
#     def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
#         # Step 1: Pair each number with its index
#         indexed = [(num, i) for i, num in enumerate(nums)]
        
#         # Step 2: Sort by value (descending), pick top k
#         top_k = sorted(indexed, key=lambda x: x[0], reverse=True)[:k]
        
#         # Step 3: Restore original order (sort by index)
#         top_k.sort(key=lambda x: x[1])
        
#         # Step 4: Extract the values
#         return [num for num, _ in top_k]
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        
        # Step 1: Keep top k elements in heap
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 2: Sort by index to maintain original order
        heap.sort(key=lambda x: x[1])
        
        # Step 3: Extract only the numbers
        return [num for num, _ in heap]
