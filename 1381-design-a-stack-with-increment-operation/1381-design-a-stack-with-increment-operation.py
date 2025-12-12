class CustomStack:

    def __init__(self, maxSize: int):
        self.stack= [0] *maxSize
        self.inc = [0] * maxSize
        self.curSize = 0
        

    def push(self, x: int) -> None:
        if self.curSize < len(self.stack):
            self.stack[self.curSize] =x
            self.curSize +=1
        

    def pop(self) -> int:
        if self.curSize <=0:
            return -1
        self.curSize -=1
        res= self.stack[self.curSize] + self.inc[self.curSize]
        if self.curSize >0:
            self.inc[self.curSize -1] += self.inc[self.curSize]
        self.inc[self.curSize]=0
        return res

        

    def increment(self, k: int, val: int) -> None:
        targetind=min(k,self.curSize) -1
        if targetind >=0:
            self.inc[targetind] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)