from sortedcontainers import SortedList


class KthLargest(object):

    def __init__(self, k, nums):
        #self.k, self.sl = k, SortedList(nums)
        self.k=k
        self.nums=nums
        heapq.heapify(self.nums)
        while len(self.nums)>k:
            heapq.heappop(self.nums)

    def add(self, val):
        #self.sl.add(val)  # Note that sl is a SortedList
        #return self.sl[-self.k]
        heapq.heappush(self.nums,val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)