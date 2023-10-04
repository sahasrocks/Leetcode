class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        a=list(a)
        return a==a[::-1]
        