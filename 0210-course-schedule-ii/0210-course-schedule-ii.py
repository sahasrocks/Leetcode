class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq={c:[] for c in range(numCourses)}
        for cre,pre in prerequisites:
            prereq[cre].append(pre)
        cycle=set()
        visit=set()
        output=[]
        def dfs(cre):
            if cre in cycle:
                return False
            if cre in visit:
                return True
            cycle.add(cre)
            for pre in prereq[cre]:
                if dfs(pre) == False:
                    return False
            visit.add(cre)                    
            cycle.remove(cre)
            output.append(cre)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output            