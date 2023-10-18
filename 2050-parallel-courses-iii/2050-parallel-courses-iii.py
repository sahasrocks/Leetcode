class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # List of successors
        nodeToNext = {node: [] for node in range(n)}
        # Number of prerequisites
        nodeToPrev = {node: 0 for node in range(n)}
        for prev, nextt in relations:
            nodeToNext[prev-1].append(nextt-1)
            nodeToPrev[nextt-1] += 1
        
        heap = []
        # Find start nodes without prerequisites
        for node, prevCnt in nodeToPrev.items():
            if prevCnt == 0:
                heappush(heap, (time[node], node))
        
        while heap:
            # Get the node with the earliest endtime
            tm, node = heappop(heap)
            for nextt in nodeToNext[node]:
                # Decrease counter of successor
                nodeToPrev[nextt] -= 1
                if nodeToPrev[nextt] == 0:
                    # If there are no prerequisites 
                    # add successor to processing
                    heappush(heap, (tm + time[nextt], nextt))
        
        return tm