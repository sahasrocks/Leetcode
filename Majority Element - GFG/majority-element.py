#User function template for Python 3

class Solution:
    def majorityElement(self, arr, N):
        #Your code here
        map = {}
        for i in range(0, N):
            if arr[i] in map.keys():
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1
        for key in map:
           if map[key] > (N / 2):
              return key
        return -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends