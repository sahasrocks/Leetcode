class Solution(object):
    def longestCommonPrefix(self, a):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        for i in range(len(a[0])):
            for s in a:
                if i==len(s) or s[i] !=a[0][i]:
                    return res
            res+=a[0][i]
        return res            
        
        