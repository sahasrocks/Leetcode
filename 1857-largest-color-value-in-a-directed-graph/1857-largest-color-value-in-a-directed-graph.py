class Solution:
    class CycleException(Exception):
        pass
    
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        letters=string.ascii_lowercase
        n = len(colors)
        # for each node N, maintain a list of all color values (for the graph rooted at N)
        color_values=[[1 if colors[node] == char else 0 for char in letters] for node in range(n)]
        
        # adjacency list for the graph
        children=[[] for node in range(n)]
        for parent, child in edges:
            children[parent].append(child)
            if parent == child:
                return -1
                
        def update_color_values(parent, child):
            parent_values=color_values[parent]
            child_values=color_values[child]
            for i in range(len(letters)):
                path_value = child_values[i]
                if colors[parent] == letters[i]:
                    path_value += 1
                parent_values[i] = max(parent_values[i], path_value)
                
        # keep track of nodes we have completely calculated
        complete = set() 
        # keep track of parents so that we can detect cycles
        parents=set()
        def dfs(root: int):
            if root in complete:
                return
            if root in parents:
                raise Solution.CycleException
            parents.add(root)
            for child in children[root]:
                dfs(child)
                update_color_values(root, child)
            parents.remove(root)
            complete.add(root)
            
        largest = 0
        for node in range(n):
            try: 
                dfs(node)
            except Solution.CycleException:
                return -1
            largest = max(largest,max(color_values[node]))
        return largest