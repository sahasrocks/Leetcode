class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap=defaultdict(list)
        for cre,pre in prerequisites:
            preMap[cre].append(pre)
        cycle=set()
        visited=set()
        output=[]
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            visited.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output                         


        
        # prereq={c:[] for c in range(numCourses)}
        # for cre,pre in prerequisites:
        #     prereq[cre].append(pre)
        # cycle=set()
        # visit=set()
        # output=[]
        # def dfs(cre):
        #     if cre in cycle:
        #         return False
        #     if cre in visit:
        #         return True
        #     cycle.add(cre)
        #     for pre in prereq[cre]:
        #         if dfs(pre) == False:
        #             return False
        #     visit.add(cre)                    
        #     cycle.remove(cre)
        #     output.append(cre)
        #     return True
        # for c in range(numCourses):
        #     if dfs(c) == False:
        #         return []
        # return output            