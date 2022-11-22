from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q=deque([[n,0]])
        have_been_put = [0 for i in range(n+1)]
        while q:
            num,res = q.popleft()
            if num==0:
                break
            for j in range(1,int(num**0.5)+1):
                if(have_been_put[num-j*j] !=1):
                    q.append([num-j*j,res+1])
                have_been_put[num-j*j] = 1
        return res