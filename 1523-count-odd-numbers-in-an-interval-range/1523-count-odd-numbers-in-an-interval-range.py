class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l= high - low +1
        count = l //2
        if l % 2 and low %2:
            count +=1
        return count            

        # count = math.ceil((high-low)/2)
        # if (high % 2 != 0 and low % 2 !=0):
        #     count+=1
        # return count