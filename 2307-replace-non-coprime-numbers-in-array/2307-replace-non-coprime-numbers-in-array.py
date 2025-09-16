from fractions import gcd   # Python 2

class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []
        
        for num in nums:
            while stack and gcd(stack[-1], num) > 1:
                top = stack.pop()
                num = (top * num) // gcd(top, num)
            
            stack.append(num)
        
        return stack
