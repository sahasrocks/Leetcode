from functools import cache
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(N)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        @cache
        def dp(i, j) -> tuple[int, int]:
            size, tot = map(
                sum, zip(*(dp(k, i) for k in graph[i] if k != j))
            ) if len(graph[i]) > 1 else (0, 0)
            return size + 1, tot + size
 
        return [
            N - 1 + sum(dp(edge, i)[1] for edge in graph[i])
            for i in range(N)
        ]
        