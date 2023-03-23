class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # you need at least n - 1 edges to connect n nodes
        if n - 1 > len(connections):
            return -1
        
        link = list(range(n))
        size = n * [1]
        conCount = 1
        
        def find(x):
            while x != link[x]:
                x = link[x]
            return x
        
        def same(a, b):
            return find(a) == find(b)
        
        def unite(a, b):
            a, b = find(a), find(b)
            if size[a] < size[b]:
                a, b = b, a
            size[a] += size[b]
            link[b] = a
        
        for a, b in connections:
            if not same(a, b):
                unite(a, b)
                conCount += 1
        
        return n - conCount