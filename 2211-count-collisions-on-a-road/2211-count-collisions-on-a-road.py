class Solution:
    def countCollisions(self, directions: str) -> int:
        n=len(directions)
        if n==1:
            return 0
        l,r=0,n-1
        while l<r and directions[l]=='L':
            l+=1
        while l<r and directions[r]=='R':
            r-=1
        if l>=r:
            return 0
        return sum(directions[i] !='S' for i in range(l,r+1))                

        
        
        # ans = 0
        # # At the beginning, leftest car can go without collide
        # # At the beginning, rightest car can go without collide
        
        # leftc = rightc = 0
        
        # for c in directions:
        #     # if left side, no car stop or right answer + 0
        #     # if left side start to have car go right or stop
        #     # then cars after that are bound to be stopped so answer + 1
        #     if c == "L":
        #         ans += leftc
        #     else:
        #         leftc = 1
                
        # for c in directions[::-1]:
        #     # if right side, no car stop or left answer + 0
        #     # if right side start to have car go left or stop
        #     # then cars after that are bound to be stopped so answer + 1
        #     if c == "R":
        #         ans += rightc
        #     else:
        #         rightc = 1
       
        # return ans