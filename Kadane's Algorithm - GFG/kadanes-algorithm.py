#User function Template for python3

class Solution:
    def maxSubArraySum(self, arr, N):
        maxsum = 0
        currentsum = 0
        if max(arr) <= 0:
            return max(arr)
        for i in arr:
            currentsum += i
            if currentsum > maxsum:
                maxsum = currentsum
            elif currentsum < 0:
                currentsum = 0
        return maxsum   
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends