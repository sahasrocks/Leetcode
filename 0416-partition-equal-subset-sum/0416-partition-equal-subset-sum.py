class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        n=len(nums)
        dp=[[-1]*(target+1) for i in range(n+1)]
        def dfs(i,target):
            if target==0:
                return True
            if i>=n or target<0:
                return False
            if dp[i][target] !=-1:
                return dp[i][target]
            dp[i][target]=dfs(i+1,target) or dfs(i+1,target-nums[i])
            return dp[i][target]
        return dfs(0,target)                    
        # if sum(nums)%2:
        #     return False
        # target=sum(nums)//2
        # n=len(nums)
        # dp=[[-1]*(target+1) for i in range(n+1)]
        # def dfs(i,target):
        #     if target==0:
        #         return True
        #     if i>=n or target<0:
        #         return False
        #     if dp[i][target] != -1:
        #         return dp[i][target]
        #     dp[i][target] = dfs(i+1,target) or dfs(i+1,target-nums[i])
        #     return dp[i][target]
        # return dfs(0,target)                    
        
        
        # if sum(nums) % 2:
        #     return False
        # dp=set()
        # dp.add(0)
        # target=sum(nums)//2
        # for i in range(len(nums)-1,-1,-1):
        #     nextDP=set()
        #     for j in dp:
        #         nextDP.add(j+nums[i])
        #         nextDP.add(j)
        #     dp=nextDP
        # return True if target in dp else False            
        