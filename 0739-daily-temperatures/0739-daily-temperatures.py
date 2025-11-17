class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0] * len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackInd=stack.pop()
                res[stackInd]=i-stackInd
            stack.append([t,i])
        return res        
        
        
        # res = []
        # n = len(temperatures)
        # for i in range(n):
        #     days_to_wait = 0
        #     for j in range(i + 1, n): # Start searching from the next day (i + 1)
        #         days_to_wait += 1
        #         if temperatures[j] > temperatures[i]:
        #             res.append(days_to_wait)
        #             break
        #     else: # This 'else' executes if the 'for j' loop completes without a 'break'
        #         res.append(0) # No warmer day found, so append 0
        # return res          
        
        
        
        
        
        
        
        
        # l = len(temperatures)
        # result, stack = [0]*l, deque()
        # for i in range(l):
        #     while stack and temperatures[stack[-1]] < temperatures[i]:
        #         index = stack.pop()
        #         result[index] = i-index
        #     stack.append(i)
        # return result