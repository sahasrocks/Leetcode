class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        y=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        a=b=0
        for i in range(len(s)//2):
            
            if s[i] in y:
                a+=1
            if s[len(s)//2 + i] in y:
                b+=1
                
        return a==b