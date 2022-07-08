class Solution:
    def maxSumDivThree(self, N: List[int]) -> int:
        A, B, S = heapq.nsmallest(2,[n for n in N if n % 3 == 1]), heapq.nsmallest(2,[n for n in N if n % 3 == 2]), sum(N)
        if S % 3 == 0: return S
        if S % 3 == 1: return S - min(A[0], sum(B) if len(B) > 1 else math.inf)
        if S % 3 == 2: return S - min(B[0], sum(A) if len(A) > 1 else math.inf)