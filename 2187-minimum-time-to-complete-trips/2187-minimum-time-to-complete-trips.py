class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, time[0] * totalTrips
        while l < r:
            m = (l + r) // 2
            if sum(m // t for t in time) < totalTrips:
                l = m + 1
            else:
                r = m
        return l