class Solution:
    def isValid(self, s: str) -> bool:
        leftl = []
        for c in s:
            if c in ['(','{','[']:
                leftl.append(c)
            elif c==')' and len(leftl) !=0 and leftl[-1]== '(':
                leftl.pop()
            elif c=='}' and len(leftl) !=0 and leftl[-1]== '{':
                leftl.pop()
            elif c==']' and len(leftl) !=0 and leftl[-1]== '[':
                leftl.pop()    
            else :
                return False
        return leftl ==[]    