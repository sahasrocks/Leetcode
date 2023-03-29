class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        while sum(satisfaction)<0:
            satisfaction.pop()
        total=0
        l=len(satisfaction)
        for i in range(l):
            total+=satisfaction[i]*(l-i)
        return total