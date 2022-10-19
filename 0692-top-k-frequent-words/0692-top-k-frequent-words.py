class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        myC=collections.Counter(words)
        
        return [w for w,v in sorted(myC.items(), key=lambda x:(-x[1],x[0]))][:k]