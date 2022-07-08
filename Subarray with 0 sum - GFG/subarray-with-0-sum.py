#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        sum = 0
        hashmap = {}
        for i in arr:
            if i == 0:
                return True
            sum += i
           
            if sum == 0:
                return True
           
            if sum not in hashmap.keys():
                hashmap[sum] = 1
            else:
                hashmap[sum]+= 1
               
           
        for i in hashmap.values():
            if i > 1:
                return True
           
        return False    

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends