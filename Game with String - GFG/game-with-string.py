#User function Template for python3

class Solution:
    def minValue(self, s, k):
        # code here
        from collections import Counter
        import heapq

   
        d = Counter(s)
        c = list(d.values())
       # c.sort(reverse=True)
        c = [i*-1 for i in c]
        heapq.heapify(c)
        while k>0:
            temp = heapq.heappop(c)
            temp +=1
            heapq.heappush(c, temp)
            k-=1
        summ = 0
        for i in c:
            summ+=i**2
        return summ

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends