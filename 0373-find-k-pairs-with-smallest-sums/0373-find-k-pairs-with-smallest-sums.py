class Solution:
    def kSmallestPairs(self, num1: List[int], num2: List[int], k: int) -> List[List[int]]:
        if not num1 or not num2 or k==0:
            return []
        res=[]
        heap=[]
        for i in range(min(len(num1),k)):
            heapq.heappush(heap,(num1[i]+num2[0],i,0))
        while k>0 and heap:
            total,i,j=heapq.heappop(heap)
            res.append([num1[i],num2[j]])
            if j+1<len(num2):
                heapq.heappush(heap,(num1[i]+num2[j+1],i,j+1))
            k-=1
        return res                
        
        
        # def generator(n1):
        #     for n2 in nums2:
        #         yield [n1+n2, n1, n2]
        # merged = heapq.merge(*map(generator, nums1))
        # return [p[1:] for p in itertools.islice(merged, k) if p]