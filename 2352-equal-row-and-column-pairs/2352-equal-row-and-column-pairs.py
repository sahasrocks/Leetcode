class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(map(tuple, grid))
        cols = Counter(map(tuple, zip(*grid)))
        return sum(v * cols.get(tuple(k), 0) for k, v in rows.items())
