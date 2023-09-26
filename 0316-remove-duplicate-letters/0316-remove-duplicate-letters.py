class Solution:
    def removeDuplicateLetters(self, s):
        last_index = {}
        for k, v in enumerate(s):
            last_index[v] = k

        stack = []
        visited = set()

        for i in range(len(s)):
            if s[i] in visited:
                continue

            while stack and stack[-1] > s[i] and last_index[stack[-1]] > i:
                visited.remove(stack[-1])
                stack.pop()
            
            stack.append(s[i])
            visited.add(s[i])
        
        return "".join(stack)