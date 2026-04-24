class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l,r,a=0,0,0
        n=len(moves)
        for i in moves:
            if i=='R':
                r+=1
            elif i=='L':
                l+=1
            else:
                a+=1
        return a+abs(r-l)