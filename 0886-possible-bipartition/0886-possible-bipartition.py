class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        
        adj=defaultdict(list)
        for x,y in dislikes:
            adj[x].append(y)
            adj[y].append(x)
        
        colors=[-1]*(n+1)
        
        def bfs(start):
            colors[start]=0
            q=[]
            q.append(start)
            
            while q:
                s=q.pop(0)
                for node in adj[s]:
                    if colors[node]==-1:
                        colors[node]=1-colors[s]
                        q.append(node)
                    else:
                        if colors[node]==colors[s]:
                            return False
            return True
        
        for i in range(1,n+1):
            if colors[i]==-1:
                if bfs(i)==False:
                    return False
        return True
        