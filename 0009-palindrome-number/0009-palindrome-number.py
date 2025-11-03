class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        y = s[::-1]
        return y==s