class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res=1e9
        n=len(words)
        for i,e in enumerate(words):
            if e==target:
                diff=abs(startIndex-i)
                res=min(res,diff,n-diff)
        return res if res !=1e9 else -1        