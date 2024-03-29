class Solution:
    
    
#     def fib(self, n: int) -> int:
#         if n<=1:
#             return n
        
#         else:
#             return self.fib(n-1)+self.fib(n-2)
    def fib(self, n):
        
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]    
    # def fib(self, n):
    #     if n==0:
    #         return 0
    #     if n==1:
    #         return 1
    #     a,b=0,1
    #     for i in range(2,n+1):
    #         a,b=b,a+b
    #     return b  
    # def fib(self, n):
    #     dp=[-1]*(n+1)
    #     for i in range(n+1):
    #         if i <=1:
    #             dp[i]=i
    #         else:
    #             dp[i]=dp[i-1] +dp[i-2]
    #     return dp[n]        
            
                