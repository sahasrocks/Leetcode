#User function Template for python3

class Solution:
    def findTwoElement( self,A, n): 
        # code here
        n = len(A)
        
        for i in range(n):
            x = A[i] % (n+1)
            A[x-1] += n+1
        
        ans = [None,None]
        for i in range(n):
            if A[i] //(n+1) > 1:
                ans[0] = i+1
            if A[i] // (n+1) < 1:
                ans[1] = i+1
        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends