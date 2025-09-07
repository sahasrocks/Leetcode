class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a=[]
        for i in range(n//2):
            a.append(i+1)
            a.append((-1)*(i+1))
        if n%2==1:
            a.append(0)
        return a                   

        