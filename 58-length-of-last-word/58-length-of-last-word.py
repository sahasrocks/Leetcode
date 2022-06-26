class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        import re

        
        wordList = re.sub("[^\w]", " ",  s).split()
        a = len(wordList)
        b = wordList[a-1]
        str(b)
        return len(b)