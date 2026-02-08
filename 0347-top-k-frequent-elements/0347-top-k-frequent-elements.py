class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # c= Counter(nums)
        
        # return [num for num, _ in c.most_common(k)]
        c=defaultdict(int)
        for n in nums:
            c[n]+=1
        heap=[]
        for num in c.keys():
            heapq.heappush(heap,(c[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res                
        # c=defaultdict(int)
        # for n in nums:
        #     c[n]+=1
        # heap=[]
        # for num in c.keys():
        #     heapq.heappush(heap,(c[num],num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # res=[]
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res                
        
        
        # count={}
        # for num in nums:
        #     count[num]=1+count.get(num,0)
        # heap=[]
        # for num in count.keys():
        #     heapq.heappush(heap,(count[num],num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # res=[]
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res                    
        
        
        
        
        
        
        
        
        
        
        
        # count={}
        # for num in nums:
        #     count[num]=1+count.get(num,0)
        # heap=[]
        # for num in count.keys():
        #     heapq.heappush(heap,(count[num],num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # res=[]
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res            



        # counter = Counter(nums)
        # return [num for num, _ in counter.most_common(k)]

        