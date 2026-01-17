class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols=len(heights),len(heights[0])
        visit=set()
        minHeap=[(0,0,0)]
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        while minHeap:
            diff,r,c=heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c)==(rows-1,cols-1):
                return diff
            for dr,dc in dirs:
                nr,nc = dr+r,dc+c
                if ( nr<0 or nr>=rows or nc<0 or nc>=cols or (nr,nc) in visit ):
                    continue
                newDiff = max(diff,abs(heights[r][c]-heights[nr][nc]))
                heapq.heappush(minHeap,(newDiff,nr,nc))
        return 0                
        