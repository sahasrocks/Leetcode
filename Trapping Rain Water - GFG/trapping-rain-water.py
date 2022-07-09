
class Solution:
    def trappingWater(self, a,n):
        #Code here
        left = 0
        right = n-1
        i = 0
        j = n-1
        vol = 0
        while i <= j:
            while i <= j and a[i] <= a[j]:
                if a[i] <= a[left]:
                    vol += a[left] - a[i]
                    i += 1
                else:
                    left = i
            while i <= j and a[j] < a[i]:
                if a[right] >= a[j]:
                    vol += a[right] - a[j]
                    j -= 1
                else:
                    right = j
        return vol

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends