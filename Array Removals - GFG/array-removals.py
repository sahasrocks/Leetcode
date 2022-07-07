#User function Template for python3


class Solution:

    def removals(self,arr, n, k):
         
      # sort the array
      arr.sort()
      dp = [0 for i in range(n)]
     
      # Fill all stated with -1
      # when only one element
      for i in range(n):
        dp[i] = -1
     
      # As dp[0] = 0 (base case) so min
      # no of elements to be removed are
      # n-1 elements
      ans = n - 1
      dp[0] = 0
       
      for i in range(1, n):
        dp[i] = i
        j = dp[i - 1]
         
        while (j != i and arr[i] - arr[j] > k):
          j += 1
           
        dp[i] = min(dp[i], j)
        ans = min(ans, (n - (i - j + 1)))
         
      return ans   

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends