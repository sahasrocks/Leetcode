class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=collections.defaultdict(list)
        for i,eq in enumerate(equations):
            a,b=eq
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])

        def bfs(src,target):
            if not src in adj or not target in adj:
                return -1
            q=deque()
            visit=set()
            q.append([src,1])

            visit.add(src)
            while q:
                n,w=q.popleft()
                if n==target:
                    return w
                for nei,weight in adj[n]:
                    if nei not in visit:
                        q.append([nei,w*weight])
                        visit.add(nei)
            return -1
        #return [bfs(q[0],q[1]) for q in queries]
        def dfs(src, target, visited):
            if src not in adj or target not in adj:
                return -1.0
            if src == target:
                return 1.0
            
            visited.add(src)
            for nei, val in adj[src]:
                if nei not in visited:
                    res = dfs(nei, target, visited)
                    if res != -1.0:
                        return val * res  # Multiply the path ratio
            return -1.0
        
        # Step 3: Process each query
        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        return results
                            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def bfs(source, target, value):
        #     queue = [[source, value]]
        #     visited = set()
        #     while queue:
                
        #         node, val = queue.pop(0)
        #         if node == target:
        #             return val
        #         if node in visited:
        #             continue
        #         visited.add(node)
                
        #         for baju_wala in graph[node]:
        #             if baju_wala not in visited:
        #                 new_val = val * graph[node][baju_wala]
        #                 queue.append([baju_wala, new_val])
            
        #     return float(-1)
                
        
        # graph = {}
        # for i in range(len(values)):
        #     u, v = equations[i]
        #     value = values[i]
        #     rev_value = 1 / value
        #     if u in graph:
        #         graph[u][v] = value
        #     else:
        #         graph[u] = {v: value}
        #     if v in graph:
        #         graph[v][u] = rev_value
        #     else:
        #         graph[v] = {u: rev_value}
        
        
        # result = []
        # for a, b in queries:
        #     if a not in graph or b not in graph:
        #         result.append(float(-1))
        #     else:
        #         res = bfs(a, b, 1)
        #         result.append(res)
                
        
        # return result