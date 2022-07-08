#User function Template for python3

class Solution:
    def solve(self, arr, n):
        # code here
        if n==1:
            return str(arr[0])
        arr.sort()
        s1=""
        s2=""
        for i in range(n):
            if i%2==0:
                s1+=str(arr[i])
            else:
                s2+=str(arr[i])
        ans=int(s1)+int(s2)
        ans=str(ans)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends