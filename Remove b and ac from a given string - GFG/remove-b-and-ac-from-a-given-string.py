#User function Template for python3

class Solution:
    def stringFilter(self, str):
        # code here
        
        s=str.replace("ac","").replace("b","")
        return s
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.stringFilter(s)
        print(ans)
# } Driver Code Ends