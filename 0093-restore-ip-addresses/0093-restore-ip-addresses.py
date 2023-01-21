class Solution:
    def __init__(self):
        self.ans=[]
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.recurse(s,3,0)
        return self.ans
    
    def recurse(self,s:str,dots:int,idx:int)->None:
        if dots==0:
            if self.isValid(s[idx:]): 
                self.ans.append(s)
            return 
        dots-=1
        self.recurse(s[:idx+1]+"."+s[idx+1:],dots,idx+2)
        if self.isValid(s[idx:idx+2]):
            self.recurse(s[:idx+2]+"."+s[idx+2:],dots,idx+3)
        if self.isValid(s[idx:idx+3]):
            self.recurse(s[:idx+3]+"."+s[idx+3:],dots,idx+4)
        
    def isValid(self,s:str)->bool:
        if len(s)==0:
            return False
        if len(s)==1: 
            return True
        if len(s)==2: 
            return (s[0]!="0")
        return (s[0]!="0") and int(s)<=255