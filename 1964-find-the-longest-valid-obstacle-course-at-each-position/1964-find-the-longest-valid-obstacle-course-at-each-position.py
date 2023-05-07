class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        mono=[]
        ans=[]
        for obstacl in obstacles:
            i=bisect.bisect(mono,obstacl)
            ans.append(i+1)
            if i==len(mono):
                mono.append(0)

            mono[i]=obstacl

        return ans