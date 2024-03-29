class Solution:
    def allPathsSourceTarget(self, g, cur=0):
        if cur == len(g) - 1: return [[len(g) - 1]]
        return [([cur] + path) for i in g[cur] for path in self.allPathsSourceTarget(g, i)]