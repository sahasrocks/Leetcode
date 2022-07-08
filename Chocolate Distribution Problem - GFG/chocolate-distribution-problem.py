#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()

	
    	w_start = 0
    	ans = float('inf')
            
    	
    	for w_end in range(N):
    		if (w_end - w_start + 1) == M:
    			ans = min(ans, A[w_end] - A[w_start])
    			w_start += 1
    			w_end = w_start
            
    	
    	return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends