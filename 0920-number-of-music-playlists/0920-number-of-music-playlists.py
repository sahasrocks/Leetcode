class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        M = 10 ** 9 + 7
        def solve(n, goal, k):
            res = 1
            for i in range(goal):
                res = (res * n) % M
                if n == 0: break
                if k > 0:
                    n -= 1
                    k -= 1
            return res
        res = 0
        sign = 1
        for j in range(n,-1,-1):
            res = (res + sign*math.comb(n,j)*solve(j,goal,k)) % M
            sign *= -1
        return res % M