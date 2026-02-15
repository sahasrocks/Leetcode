class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s,i=0,x
        while i:
            s+=i%10
            i//=10
        return -1 if x %s else s         
        