class Solution:
    def findKthLargest(self, nums, k):
        min_heap=[]
        for n in nums:
            if len(min_heap)<k:
                heapq.heappush(min_heap,n)
            else:
                heapq.heappushpop(min_heap,n)
        return min_heap[0]            
        
        # min_heap=[]
        # for n in nums:
        #     if len(min_heap)<k:
        #         heapq.heappush(min_heap,n)
        #     else:
        #         heapq.heappushpop(min_heap,n)
        # return min_heap[0]            
        
        # min_heap=[]
        # for n in nums:
        #     if len(min_heap)<k:
        #         heapq.heappush(min_heap,n)
        #     else:
        #         heapq.heappushpop(min_heap,n)
        # return min_heap[0]            
        # min_heap=[]
        # for n in nums:
        #     if len(min_heap)<k:
        #         heapq.heappush(min_heap,n)
        #     else:
        #         heapq.heappushpop(min_heap,n)
        # return min_heap[0]           

        # min_heap=[]
        # for num in nums:
        #     if len(min_heap)<k:
        #         heapq.heappush(min_heap,num)
        #     else:
        #         heapq.heappushpop(min_heap,num)
        # return min_heap[0]            
        
        
        
        
        
        # pivot = nums[0]
        # left  = [l for l in nums if l < pivot]
        # equal = [e for e in nums if e == pivot]
        # right = [r for r in nums if r > pivot]

        # if k <= len(right):
        #     return self.findKthLargest(right, k)
        # elif (k - len(right)) <= len(equal):
        #     return equal[0]
        # else:
        #     return self.findKthLargest(left, k - len(right) - len(equal))    