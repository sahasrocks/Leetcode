class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for c in s:
            if 'a' <= c <= 'z':
                result += c

            elif c == '*':
                if result:
                    result = result[:-1]

            elif c == '#':
                result += result

            elif c == '%':
                result = result[::-1]

        return result