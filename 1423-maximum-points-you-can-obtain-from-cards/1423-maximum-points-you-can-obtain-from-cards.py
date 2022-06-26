class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        best = points = sum(cardPoints[:k])
        for right, left in enumerate(range(k-1, -1, -1)):
            points += cardPoints[-right-1] - cardPoints[left]
            best = max(best, points)
        return best