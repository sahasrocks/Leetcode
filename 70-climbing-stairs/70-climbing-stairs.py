class Solution:
    def climbStairs(self, n: int) -> int:
        
        
    	a, b = 1, 1
    	for i in range(n): 
    	    a, b = b, a + b
    	return a
        # if n<=2:
        #     return n
        # return (self.climbStairs(n - 1) + self.climbStairs(n - 2))