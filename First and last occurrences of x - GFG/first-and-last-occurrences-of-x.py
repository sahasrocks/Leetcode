#User function Template for python3


def find(arr,n,x):
    if n==0:
        return [-1,-1]
    l=[]
    for i in range(n):
        if arr[i]==x:
            l.append(i)
    if len(l)==0:
        return [-1,-1]
    return [l[0],l[-1]]
        


#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends