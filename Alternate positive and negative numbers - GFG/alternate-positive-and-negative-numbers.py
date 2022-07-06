#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        a=[]
        b=[]
        for i in range(n):
           if arr[i]<0:
               a.append(arr[i])
           elif arr[i]>=0:
               b.append(arr[i])
        arr.clear()
        if len(b)>len(a):
            l=len(b)
        else:
            l=len(a)
        s=0
        for i in range(0,l,1):
            if i>(len(b)-1):
                s+=1
            else:
                arr.append(b[i])
            if i>(len(a)-1):
                s+=1
            else:
                arr.append(a[i])
        return arr        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends