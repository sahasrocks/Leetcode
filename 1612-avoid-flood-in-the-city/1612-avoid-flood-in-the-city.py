from sortedcontainers import SortedList as sl
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1]*(len(rains))
        has_rained = dict()
        free = sl()
        for i in range(len(rains)):
            # print(free)
            if rains[i]==0:
                free.add(i)
            else:
                if rains[i] not in has_rained:
                    has_rained[rains[i]]=i
                else:
					# no free days are available
                    if len(free)==0:
                        return []
					#finding the index of the free day that came after the first occurance of
					# rains[i]
                    idx = free.bisect_left(has_rained[rains[i]])
                    # print(free,idx,i,has_rained)
                    if idx<len(free):
                        ans[free[idx]]=rains[i]
						# updating the index of rains[i] for future it's future occurances
                        has_rained[rains[i]] = i
                        free.remove(free[idx])
                    else:
						#if no such index exists then return
                        return []
        if len(free):
            while free:
				# choosing some day to dry on the remaining days
                ans[free.pop()]=1
        return ans