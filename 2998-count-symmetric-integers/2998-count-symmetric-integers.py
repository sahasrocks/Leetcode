class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        a=0
        for i in range(low, high+1):
            s=str(i)
            if len(s) %2 !=0:
                continue
            mid=len(s)//2
            left=sum(int(d) for d in s[:mid])
            right= sum(int(d) for d in s[mid:])
            if left==right:
                a+=1
        return a            

        