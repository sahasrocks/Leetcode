class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r=0,len(cardPoints)-k
        total=sum(cardPoints[r:])
        res=total

        while r<len(cardPoints):
            total+= (cardPoints[l]-cardPoints[r])
            l+=1
            r+=1
            res=max(res,total)
        return res    
        
        
        
        
        
        
        
        
        
        
        
        
        
        # best = points = sum(cardPoints[:k])
        # for right, left in enumerate(range(k-1, -1, -1)):
        #     points += cardPoints[-right-1] - cardPoints[left]
        #     best = max(best, points)
        # return best