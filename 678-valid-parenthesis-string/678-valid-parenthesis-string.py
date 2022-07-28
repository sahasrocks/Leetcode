class Solution:
    def checkValidString(self, s: str) -> bool:
            loOpen = hiOpen = 0  # possible number of open left brackets
            for c in s:
                if c == '(':
                    loOpen, hiOpen = loOpen+1, hiOpen+1
                elif c == ')':
                    loOpen, hiOpen = loOpen-1, hiOpen-1
                else:
                    loOpen, hiOpen = loOpen-1, hiOpen+1
                if hiOpen < 0: return False
                loOpen = max(0, loOpen)        

            return loOpen == 0
        