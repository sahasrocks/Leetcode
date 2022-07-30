class Solution:
    def insert(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
#         merged,t,l = [], 0, len(intervals)       
#         for curr in intervals:
            
#             # If interval[i] completely smaller than new one
#             if new[0]>curr[1]:
#                 merged.append(curr)
             
   
#             elif curr[0]>new[1]:
#                 break
             
#             # If interval[i] is overlapping with new
#             else:              
#                 # choose minm and maxm boundaries from both
#                 new[0] = min(new[0], curr[0])
#                 new[1] = max(new[1], curr[1])
            
#             t+=1
            
#         # Apeending last new interval
#         merged.append(new)
        
#         return merged+intervals[t:] if t<l else merged
            