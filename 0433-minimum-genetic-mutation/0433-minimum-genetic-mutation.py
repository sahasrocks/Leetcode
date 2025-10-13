class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank=set(bank)
        if end not in bank:
            return -1
        q =deque()
        q.append([start,0])
        visit=set()
        visit.add(start)
        while q:
            gene,level=q.popleft()
            if gene==end:
                return level
            for i in range(len(gene)):
                for letters in 'ACGT':
                    new_gene=gene[:i] + letters + gene[i+1:] 
                    if new_gene not in visit and new_gene in bank:
                        q.append([new_gene,level+1])
                        visit.add(new_gene)
        return -1               

        
        
        
        
        
        
        
        
        
        
        
        
        
        # bank, v, q = set(bank), {start}, [(start, 0)]
        # for g,k in q:
        #     for s in (g[:i] + cc + g[i+1:] for i,c in enumerate(g) for cc in 'ACGT'):
        #         if s in bank and s not in v:
        #             if s==end:
        #                 return k+1
        #             q.append((s, k+1))
        #             v.add(s)
        # return -1