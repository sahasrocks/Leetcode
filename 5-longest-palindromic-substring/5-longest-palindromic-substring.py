class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = ''
        maxp = ''

        for i in range(len(s)):
            temp += s[i]
            for j in range(len(temp)):
                if temp[j] == s[i] and s[j:i+1] == s[j:i+1][::-1] and len(s[j:i+1]) > len(maxp):
                    maxp = s[j:i+1]
                    break

        return maxp                