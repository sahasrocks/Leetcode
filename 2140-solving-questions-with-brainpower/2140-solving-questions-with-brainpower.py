class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = [-1] * len(questions)
        def dp(i):
            if i >= len(questions):
                return 0
            
            if memo[i] != -1:
                return memo[i]

            # skip i th question and go to next 
            skip = dp(i+1) 
            # solve i th question and go to next available question
            solve = questions[i][0] + dp(i+questions[i][1]+1) 

            memo[i] = max(skip, solve)
            return memo[i]
        
        return dp(0)