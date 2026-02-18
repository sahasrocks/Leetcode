# class Solution:
# 	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

# 		preMap={i:[] for i in range(numCourses)}
#         for crs,pre in prerequisites:

#             preMap[crs].append(pre)
#         visitSet=set()
#         def dfs(crs):
#             if crs in visitSet:
#                 return False
#             if preMap[crs]==[]:
#                 return True
#             visitSet.add(crs)
#             for pre in preMap[crs]:
#                 if not dfs(pre):
#                     return False
#             visitSet.remove(crs)
#             preMap[crs]=[]
#             return True
#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return False
#             return True                            
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap=defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs]==[]:
                return True
            visited.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            premap[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True                                
        
        
        # premap=defaultdict(list)
        # for crs,pre in prerequisites:
        #     premap[crs].append(pre)
        # visited=set()
        # def dfs(crs):
        #     if crs in visited:
        #         return False
        #     if premap[crs]==[]:
        #         return True
        #     visited.add(crs)
        #     for pre in premap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visited.remove(crs)
        #     premap[crs]=[]
        #     return True
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True        

        
        
        # premap=defaultdict(list)
        # for crs,pre in prerequisites:
        #     premap[crs].append(pre)
        # visited=set()
        # def dfs(crs):
        #     if crs in visited:
        #         return False
        #     if premap[crs]==[]:
        #         return True
        #     visited.add(crs)
        #     for pre in premap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visited.remove(crs)
        #     premap[crs] =[]
        #     return True
        # print(premap)    
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True                               
        
        # preMap=defaultdict(list)
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)
        # visited=set()
        # def dfs(crs):
        #     if crs in visited:
        #         return False
        #     if preMap[crs] == []:
        #         return True
        #     visited.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visited.remove(crs)
        #     preMap[crs] =[]
        #     return True
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True                                
        
        
        # preMap = {i: [] for i in range(numCourses)}

        # # Build adjacency list
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)

        # visitSet = set()

        # def dfs(crs):
        #     if crs in visitSet:
        #         return False  # cycle detected
        #     if preMap[crs] == []:
        #         return True   # no prerequisites left

        #     visitSet.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visitSet.remove(crs)
        #     preMap[crs] = []  # mark as fully processed
        #     return True

        # # check all courses
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # graph=defaultdict(list)
		# indegree={}

		# #initialising dictionary
		# for i in range(numCourses):
		# 	indegree[i]=0	

		# #filling graph and indegree dictionaries
		# for child,parent in prerequisites:
		# 	graph[parent].append(child)
		# 	indegree[child]+=1

		# queue=deque()
		# for key,value in indegree.items():
		# 	if value==0:
		# 		queue.append(key)

		# courseSequence=[]
		# while queue:
		# 	course=queue.popleft()
		# 	courseSequence.append(course)
		# 	for neighbour in graph[course]:
		# 		indegree[neighbour]-=1
		# 		if indegree[neighbour]==0:
		# 			queue.append(neighbour)

		# return len(courseSequence)==numCourses