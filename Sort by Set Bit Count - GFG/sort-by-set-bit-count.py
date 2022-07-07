#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        func = lambda e:bin(e).count('1')
        arr.sort(reverse=True,key=func)
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends