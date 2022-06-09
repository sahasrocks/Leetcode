class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return sum(map(ord,coordinates)) % 2