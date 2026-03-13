from math import ceil
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        heap = [] #(Time worker is done, workerTimes[i], next time we pick worker)


        for w in workerTimes:
            heapq.heappush(heap, (w,w,1))


        answer = 0
        for _ in range(mountainHeight):

            available, time, iteration = heapq.heappop(heap)

            answer = max(answer, available)

            iteration += 1
            available += time * iteration

            heapq.heappush(heap, (available, time, iteration))
        return answer