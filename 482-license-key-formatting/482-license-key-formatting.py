class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        result = []

        count = 0
        s = s.replace('-', '')
        for index,char in enumerate(reversed(s)):
            result.append(char)
            count +=1
            if count ==k and index != len(s) -1:
                result.append('-')
                count=0

        return ''.join(reversed(result))