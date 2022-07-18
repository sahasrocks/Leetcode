class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix:
            return 0
        
        def num_for_one_row(nums):
            prev = {}
            prev[0] = 1
            cur_sum = 0
            ans = 0
            for num in nums:
                cur_sum += num
                if cur_sum - target in prev:
                    ans += prev[cur_sum - target]
                if cur_sum not in prev:
                    prev[cur_sum] = 1
                else:
                    prev[cur_sum] += 1
            return ans 
        
        res = 0
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            nums = [0]*n
            for j in range(i,m):
                for k in range(n):
                    nums[k]+=matrix[j][k]
                res += num_for_one_row(nums)
                
        return res