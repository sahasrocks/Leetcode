#User function Template for python3

class Solution:
    
        # code here
    
    def secFrequent(self, arr, n):
        from collections import OrderedDict
       # code here
        freqMap = OrderedDict()
        for i in arr:
            if i in freqMap:
                freqMap[i] += 1
            else:
                freqMap[i] = 1
       
        sorting = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)
        return(sorting[1][0])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends