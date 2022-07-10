class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        li = []
        x = l = 1
        for i in range(0, rowIndex+1):
            li.append(int(x/l))
            x *= (rowIndex-i)
            l *= i+1  
            
        return li