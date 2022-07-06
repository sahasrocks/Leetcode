#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        count = 0
        word = arr[0]
        i=0
        while(i<n):
            
            if word != arr[i][:len(word)]:
                word = word[:len(word)-1]
                count = 0
                i = 0
            else:
                count+=1
                i+=1
            if count == n:
                return word
            if len(word)==0:
                return "-1"
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends