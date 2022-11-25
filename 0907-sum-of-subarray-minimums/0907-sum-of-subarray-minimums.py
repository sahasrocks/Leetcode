class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack = [] # monotonically increasing stack
        ans = 0
        
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                prevIdx = stack.pop()
                right = i - prevIdx - 1
                left = prevIdx if not stack else prevIdx - stack[-1] - 1
                ans +=  arr[prevIdx]* (1 + left + right + left * right)
            stack.append(i)
        
        return ans % (pow(10, 9) + 7)
        