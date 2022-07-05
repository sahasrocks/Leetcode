#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        product = []
        prefix =1
        for i in range(n):
           product.append(prefix)
           prefix = prefix*nums[i]
        suffix =1
        for i in range(n-1,-1,-1):
           product[i] = suffix * product[i]
           suffix = suffix*nums[i]
        return product   
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends