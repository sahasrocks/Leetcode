#User function Template for python3

class Solution:
    def maximizeSum(self, a, n, k):
        # Your code goes here
        a= sorted(a)
        i=0
        count=0
        while i<k and i<n:
            if a[i]<0:
                count+=1
                a[i]*=-1
                i+=1
            else:
                break
        if (k-count)%2==0:
            return sum(a)
        else:
            a=sorted(a)
            a[0]*=-1
            return sum(a)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maximizeSum(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends