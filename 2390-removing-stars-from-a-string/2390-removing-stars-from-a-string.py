class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        star_count = 0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=='*'): star_count+=1
            elif(star_count>0): star_count -= 1
            else: res.append(s[i])
        res.reverse()
        return ''.join(res)