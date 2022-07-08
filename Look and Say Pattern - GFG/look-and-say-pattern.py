#User function Template for python3

class Solution:
    def lookandsay(self, n):
        self.n = n 
        if self.n == 1:
            return "1".format(str)

        # Calling our function one more time(recursion).
        s = self.lookandsay(self.n-1)
        s = str(s)

        # Setting the frequency(counter) = 0 and the result as empty string
        counter = 0 
        res = ""

        
        # Making groups for same consecutive numbers 
        for i in range(0 ,len(s)):
            counter += 1
            if i == len(s)-1 or s[i] != s[i+1]:
                res = res + str(counter) + s[i]
                counter = 0

        return res  

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends