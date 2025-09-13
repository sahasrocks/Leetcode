class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        m=len(citations)
        citations.sort()
        for i,v in enumerate(citations):
            if m-i<=v:
                return m-i
        return 0        
        