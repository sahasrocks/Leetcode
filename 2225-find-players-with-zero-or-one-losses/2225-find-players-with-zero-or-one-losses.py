class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:

        players = set(chain(*matches))                
        loses = Counter([y for _,y in matches])    

        zeros = sorted(players - set(loses))  
        ones  = sorted(filter(lambda x: loses[x]==1, players)) 

        return [zeros, ones]
        