from bisect import bisect_left
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)
        pos = [0] * n
        # Map each point to a coordinate along the perimeter [0, 4*side)
        for i, (x, y) in enumerate(points):
            if y == 0:
                pos[i] = x
            elif x == side:
                pos[i] = side + y
            elif y == side:
                pos[i] = 2 * side + (side - x)
            else:  # x == 0
                pos[i] = 3 * side + (side - y)
        pos.sort()
        
        L = 4 * side
        # Build an "extended" list to simulate wrap‐around.
        ext = pos + [p + L for p in pos]

        def canPlace(d: int) -> bool:
            # Try every starting index
            for start in range(n):
                cur = start
                last = ext[start]
                valid = True
                limit = start + n  # We only consider ext indices in [start, start+n)
                for _ in range(1, k):
                    target = last + d
                    # Look for the first index in ext[cur+1:limit] with value >= target.
                    lo = bisect_left(ext, target, cur + 1, limit)
                    if lo == limit:
                        valid = False
                        break
                    last = ext[lo]
                    cur = lo
                # Check that the wrap‐around gap (from ext[start] + L to last) is at least d.
                if valid and (ext[start] + L - last) >= d:
                    return True
            return False
        
        low, high = 0, 2 * side
        while low < high:
            mid = (low + high + 1) // 2
            if canPlace(mid):
                low = mid
            else:
                high = mid - 1
        return low