class Solution(object):
    def palindromePairs(self, words):
        result = set()
        d = {words[x]: x for x in range(len(words))}
        for i, w in enumerate(words):
            rev = w[::-1]
            l = len(w)
            for j in range(l + 1):
                if w[j:] == rev[:l-j]:
                    if rev[l-j:] in d:
                        result.add((i, d[rev[l-j:]]))
                if w[:l-j] == rev[j:]:
                    if rev[:j] in d:
                        result.add((d[rev[:j]], i))

        return [x for x in result if x[0] != x[1]]