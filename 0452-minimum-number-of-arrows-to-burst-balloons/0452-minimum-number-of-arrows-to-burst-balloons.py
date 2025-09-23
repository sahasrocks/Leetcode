class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points.sort(key=lambda p:p[1])
        # ans,arrow=0,0
        # for [start,end] in points:
        #     if ans==0 or start>arrow:
        #         ans,arrow=ans+1,end
        # return ans   
        points = sorted(points, key = lambda x: x[1])
        arrows, end = 0, -float('inf')
        for i in points:
            if i[0] > end:
                arrows += 1
                end = i[1]
        return arrows     

