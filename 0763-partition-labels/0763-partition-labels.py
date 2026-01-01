class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex={}
        for i,e in enumerate(s):
            lastIndex[e]=i
        res=[]
        size=0
        end=0
        for i,e in enumerate(s):
            size+=1
            end=max(end,lastIndex[e])
            if i==end:
                res.append(size)
                size=0
        return res            