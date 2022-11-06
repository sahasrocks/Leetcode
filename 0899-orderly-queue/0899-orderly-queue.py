class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1: return min(s[i:] + s[:i] for i in range(len(s)))
        # if k > 1, we can move any character to any position by swapping two adjacent characters
        # By swapping a number of times, 
        # e.g. "cab" 
        # eventually we could have "abc", "acb", "bca", "bac", "cba", "cab" (3 * 2 * 1 = 6 possible arrangements)
        # so the lexicographically smallest string would be the sorted string
        return "".join(sorted(s))