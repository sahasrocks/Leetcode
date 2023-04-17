class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maximum = max( candies )
        
        # check whether current kid can achieve maximum by adding extra candies
        # output by list comprehension
        return [ (candy + extraCandies) >= maximum for candy in candies ]