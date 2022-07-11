

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sta=""
        for c in s:
            if c.isalnum():
                sta+=c.lower()
                
        return sta[::-1] ==sta       
                
        
        
        
        
        a =s.lower()
        a = ''.join(ch for ch in a if ch.isalnum())
        a = a.replace(" ","") 
        a = a.replace(',', '')
        a = a.replace('.', '')
        a = a.replace(':', '')
        a = a.replace('@', '')
        a = a.replace('%', '')
        a = a.replace('#', '')
        a = a.replace('!', '')
        a = a.replace('*', '')
        print(a)
        rev = ''.join(reversed(a))
        if (a==rev):
            return True
        else:
            return False