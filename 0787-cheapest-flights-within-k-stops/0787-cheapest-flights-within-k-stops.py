class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        priceFromSrc = {}
        stepFromSrc = {}
        h = [(0, 0, src)]
        G = collections.defaultdict(list)
        
        #build graph
        for s, d, p in flights:
            G[s].append((d, p))
        
        #dijkstra
        while h:
            price, k, node = heapq.heappop(h)
            
            if node==dst: return price
            if k>K: continue
            
            for nei, price2 in G[node]:
				#explore next destination with less price or less steps
                if nei not in priceFromSrc or price+price2<=priceFromSrc[nei] or k<stepFromSrc[nei]:
                    priceFromSrc[nei] = price+price2
                    stepFromSrc[nei] = k
                    heapq.heappush(h, (price+price2, k+1, nei))
                    
        return -1