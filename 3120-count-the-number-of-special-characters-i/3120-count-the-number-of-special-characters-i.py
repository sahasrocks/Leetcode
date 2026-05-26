class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        c = 0
        word = set(word)
        for i in word:
            if i.islower():
                if i.upper() in word:
                    c += 1
        return c
        