class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        stack = []
        ans = []
        while buildings or stack:
            if not stack or(buildings and stack[0][2]>=buildings[0][0]):
                nb = buildings.pop(0)#Add new building
                heapq.heappush(stack, (-nb[2], nb[0],nb[1]))
                while buildings and buildings[0][0]==nb[0]: #Add all buildings starging with the same x coordinate
                    nb = buildings.pop(0)
                    heapq.heappush(stack, (-nb[2], nb[0],nb[1]))
                if not ans or -stack[0][0]!= ans[-1][1]:
                    ans.append([stack[0][1], -stack[0][0]])#Add a point to the answers when the newly add building expands the skyline
            else:#stack is empty or the next building is not overlapping, updating the right part
                pb = heapq.heappop(stack) #previous highest
                while stack:
                    if stack[0][2]<=pb[2]:
                        heapq.heappop(stack)#delete buildings that are covered
                    else:
                        if -stack[0][0]!= ans[-1][1]:
                            ans.append([pb[2], -stack[0][0]])
                        break
                if not stack:#add the bottom point
                    ans.append([pb[2], 0])
        return ans