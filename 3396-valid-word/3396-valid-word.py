class Solution:
    def isValid(self, word: str) -> bool:
        vowel=['a','e','i','o','u','A','E','I','O','U']
        c=0
        v=0
        n=0
        for i in word:
            if  i.isalpha():
                if i in vowel:
                    v+=1
                else:
                    c+=1
            elif i.isdigit():
                n+=1
            else:
                return False
        return True if (v>=1 and c>=1 and len(word)>=3) else False                    



        