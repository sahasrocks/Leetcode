#User function Template for python3

class Solution:
    def changeBits(self, N):
        bits = len(bin(N)[2:]);    #Getting Number of bits of the number.
        ans = pow(2,bits)-1; # Getting the Changed Number
        sub = ans-N
        return [sub,ans];

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ans = ob.changeBits(N)
        
        print(ans[0],ans[1])
# } Driver Code Ends