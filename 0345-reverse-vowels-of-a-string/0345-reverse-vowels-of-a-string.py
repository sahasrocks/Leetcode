class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        l, h = 0, len(s) - 1
        while l < h:
            if s[l] not in vowels: l += 1
            elif s[h] not in vowels: h -= 1
            else:
                s[l], s[h] = s[h], s[l]
                l += 1
                h -= 1
        return "".join(s)