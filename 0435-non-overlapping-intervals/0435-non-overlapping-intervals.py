class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans=0
        pre=intervals[0][1]
        for s,e in intervals[1:]:
            if s>=pre:
                pre=e
            else:
                ans+=1
                pre=min(pre,e)
        return ans            
        
        # intervals.sort()
        # ans=0
        # prevEnd=intervals[0][1]
        # for start,end in intervals[1:]:
        #     if start>=prevEnd:
        #         prevEnd=end

        #     else:
        #         ans+=1
        #         prevEnd=min(end,prevEnd) 

        # return ans       