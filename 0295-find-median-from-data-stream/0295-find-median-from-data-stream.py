from sortedcontainers import SortedList
class MedianFinder:
    def __init__(self):
        self.lst = SortedList()
    def addNum(self, num: int) -> None:
        self.lst.add(num)
    def findMedian(self) -> float:
        return 0 if len(self.lst) == 0 else self.lst[len(self.lst) // 2] if len(self.lst) % 2 > 0 else (self.lst[len(self.lst) // 2 - 1] + self.lst[len(self.lst) // 2]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()