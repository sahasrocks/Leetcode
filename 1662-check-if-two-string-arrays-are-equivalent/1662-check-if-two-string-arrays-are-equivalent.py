class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        d=""
        for i in word1:
            s+=i
        for j in word2:
            d+=j
        return s==d   
        