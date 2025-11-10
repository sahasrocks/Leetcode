class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        stack=[0]
        
        for n in nums:
            while len(stack)>0:
                if n>stack[-1]:
                    stack.append(n)
                    c+=1
                    break
                elif n==stack[-1]:
                    break
                else:
                    stack.pop()
        return c                   