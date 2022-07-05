#User function Template for python3

class Solution:
    def getPairsCount(self, arr, N, K):
        # code here
        count=0
        seen={}      
        for i in arr:
            c=k-i
            if c in seen:
                count+=seen[c]
            seen[i]=seen.get(i,0)+1
                
        return count     

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends