class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        empty = 0
        
        while numBottles > 0:
            total += numBottles        # drink them
            empty += numBottles        # collect empties
            numBottles = empty // numExchange   # exchange empties
            empty = empty % numExchange         # leftover empties
        return total
