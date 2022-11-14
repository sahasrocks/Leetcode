class UnionFind:
    def __init__(self, n):
        self.leaders = [i for i in range(n)]
        self.ranks = [1 for i in range(n)]
        self.cnt = n
    
    def find(self, x):
        if self.leaders[x] != x:
            self.leaders[x] = self.find(self.leaders[x])
        return self.leaders[x]

    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q: 
            return False
        self.cnt -= 1
        if self.ranks[p] < self.ranks[q]:
            self.leaders[p] = q
        elif self.ranks[p] > self.ranks[q]:
            self.leaders[q] = p
        else:        
            self.leaders[q] = p
            self.ranks[p] += 1
        return True
    
class Solution:
    def removeStones(self, stones):
        n = len(stones)
        uf = UnionFind(n)
        row, col = {}, {}
        for stone, (r, c) in enumerate(stones):
            if r not in row:
                row[r] = stone
            else:
                uf.union(row[r], stone)
            if c not in col:
                col[c] = stone
            else:
                uf.union(col[c], stone)
        return n - uf.cnt