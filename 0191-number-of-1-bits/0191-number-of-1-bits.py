class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        onc = 0
        for i in s:
            if i =="1":
                onc+=1
        print(s)        
        return onc        
            
        