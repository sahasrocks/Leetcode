class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a=list(sentence)
        b=list(set(a))
        return len(b)==26