class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]: self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]: self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        email_map = {} # email -> account_index
        
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_map:
                    ds.union(i, email_map[email])
                else:
                    email_map[email] = i
                    
        merged = collections.defaultdict(list)
        for email, index in email_map.items():
            root = ds.find(index)
            merged[root].append(email)
            
        ans = []
        for root, emails in merged.items():
            ans.append([accounts[root][0]] + sorted(emails))
        return ans