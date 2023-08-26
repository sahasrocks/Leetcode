class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[1])
        n = len(pairs)
        i = 0
        j = 1
        ans = 1
        
        while j < n:
            if pairs[i][1] < pairs[j][0]:
                ans += 1
                i = j
                j += 1
            else:
                j += 1
        return ans
        