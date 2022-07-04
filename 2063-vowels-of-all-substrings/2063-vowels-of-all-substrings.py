class Solution:
    def countVowels(self, s: str) -> int:
        return sum((i + 1) * (len(s) - i) for i, c in enumerate(s) if c in 'aeiou')