class Solution:
    def lengthOfLIS(self, nums):
        dp=[-1]*len(nums)
        def dfs(i):
            if dp[i] !=-1:
                return dp[i]
            lis=1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    lis=max(lis,1+dfs(j))
            dp[i]=lis
            return lis
        return max(dfs(i) for i in range(len(nums)))           
        
        # dp=[[-1]*(len(nums)+1) for i in range(len(nums))]
        # def dfs(i,j):
        #     if i==len(nums):
        #         return 0
        #     if dp[i][j+1] !=-1:
        #         return dp[i][j+1]    
        #     lis=dfs(i+1,j)
        #     if j==-1 or nums[j]<nums[i]:
        #         lis=max(lis,1+dfs(i+1,i))
        #     dp[i][j+1]=lis    
        #     return lis
        # return dfs(0,-1)            
        
        
        
        # n = len(nums)
        # memo = [[-1] * (n + 1) for _ in range(n)]

        # def dfs(i, j):
        #     if i == n:
        #         return 0
        #     if memo[i][j + 1] != -1:
        #         return memo[i][j + 1]

        #     LIS = dfs(i + 1, j)

        #     if j == -1 or nums[j] < nums[i]:
        #         LIS = max(LIS, 1 + dfs(i + 1, i))

        #     memo[i][j + 1] = LIS
        #     return LIS

        # return dfs(0, -1)
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp=[[-1] * (len(nums) + 1) for _ in range(len(nums))]
#         def dfs(i,j):
#             if i==len(nums):
#                 return 0
#             if dp[i][j+1] != -1:
#                 return dp[i][j+1]

#             lis = dfs(i+1,j)
#             if j==-1 or nums[j]<nums[i]:
#                 lis = max(lis,1+dfs(i+1,i))
#             dp[i][j+1]=lis    
#             return dp[i][j+1]
#         return dfs(0,-1)            
        
        
        # LIS = [1] * len(nums)

        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])
        # return max(LIS)
        