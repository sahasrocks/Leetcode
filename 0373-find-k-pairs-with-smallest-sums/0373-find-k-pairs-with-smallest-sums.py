class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def generator(n1):
            for n2 in nums2:
                yield [n1+n2, n1, n2]
        merged = heapq.merge(*map(generator, nums1))
        return [p[1:] for p in itertools.islice(merged, k) if p]