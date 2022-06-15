class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        if len(words) == 1:
            return 1
        words = sorted(words,key=lambda elem:len(elem))
        ref = { word:1 for word in words}
        for word in words:
            for index in range(len(word)):
                newWord = word[:index] + word[index+1:]
                if newWord in ref:
                    ref[word] = max(ref[word],ref[newWord] + 1)
            if word not in ref:
                ref[word] = 1
        ls = sorted(ref.items(),key=lambda elem:elem[1],reverse=True)
        return ls[0][1]