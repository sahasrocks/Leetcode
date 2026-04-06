class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        x, y, d  = 0, 0, 0
        max_distance = 0
        obstacle_set = set(map(tuple, obstacles))
        for i in commands:
            if i == -1:
                if d == len(direction)-1:
                    d = 0
                else:
                    d += 1
            elif i == -2:
                if d == 0:
                    d = len(direction)-1
                else:
                    d -= 1
            
            else:
                while i > 0 :
                    if (x + direction[d][0], y + direction[d][1]) not in obstacle_set:
                        x = x + direction[d][0]
                        y = y + direction[d][1]
                    else:
                        break
                    i -= 1
            max_distance = max(max_distance,(x*x)+(y*y))

        return max_distance

            
        