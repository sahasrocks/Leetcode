class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxi=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            if s[i]==')':
                if len(stack)==1:
                    stack.pop()
                    stack.append(i)
                    continue
                stack.pop()
                maxi=max(maxi,i-stack[-1])

        return maxi
                
        
        