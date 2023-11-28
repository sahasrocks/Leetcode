class Solution:
    def numberOfWays(self, c: str) -> int:
        MOD = 10**9 + 7

        seatsTotal = c.count('S')
        if not (seatsTotal and seatsTotal%2 == 0):
            return 0

        result = 1
        for m in re.finditer(r'S(P*)S', c[c.find('S')+1:]):
            result *= len(m.group(1)) + 1
            result %= MOD

        return result