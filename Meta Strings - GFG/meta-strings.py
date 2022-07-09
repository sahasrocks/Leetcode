#User function Template for python3
class Solution:
    def metaStrings(self, S1, S2):
        # code here
        if S1==S2:
            return 0
        f1=sorted(list(S1))
        f2=sorted(list(S2))
        if f1!=f2:
            return 0
        else:
            count=0
            for i in range(0,len(f1)):
                if S1[i]!=S2[i]:
                    count+=1
        if count==2:
            return 1
        else:
            return 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        obj = Solution()
        if obj.metaStrings(S1, S2):
            print(1)
        else:
            print(0)
# } Driver Code Ends