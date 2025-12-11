class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        res=0
        # x and y axis
        xa=[[n+1,-1] for _ in range(n+1)]
        ya=[[n+1,-1] for _ in range(n+1)]
        for x,y in buildings:
            # min and max y in this x
            xa[x][0],xa[x][1] = min(xa[x][0],y),max(xa[x][1],y)
            # min and max x in this y
            ya[y][0] ,ya[y][1]= min(ya[y][0],x),max(ya[y][1],x)
        for x,y in buildings:
            if x>ya[y][0] and x<ya[y][1] and y>xa[x][0] and y<xa[x][1]:
                res+=1
        return res
            