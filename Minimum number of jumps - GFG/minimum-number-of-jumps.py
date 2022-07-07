#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    md=0
	    cd=0
	    jump=0
	    if n==1:
	        return 0
	        
	    for i in range(n):
	        md=max(md,i+arr[i])
	        if md>=n-1:
	            return jump+1
	        elif i==md:
	            return -1
	        elif i==cd:
	            jump+=1
	            cd=md
	    return jump         
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends