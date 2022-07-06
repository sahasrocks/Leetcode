#User function Template for python3

def printFirstNegativeInteger( arr, N, k):
    # code here
    from collections import deque
    neg=deque([])
    i,j=0,0
    res=[]
    while j<N:
        if arr[j]<0:
            neg.append(arr[j])
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            if len(neg)==0:
                res.append(0)
                
            else:
                res.append(neg[0])
                if arr[i]==neg[0]:
                    neg.popleft()
            i+=1
            j+=1
    return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends