# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.stack.append(iter(nestedList))
        
    def next(self) -> int:
        # Should be called only if hasNext() is True
        return self.next_val
    
    def hasNext(self) -> bool:
        while self.stack:
            try:
                # Try to get the next element from the top iterator in the stack
                elem = next(self.stack[-1])
            except StopIteration:
                # The top iterator is exhausted, remove it from stack
                self.stack.pop()
                continue
            
            if elem.isInteger():
                self.next_val = elem.getInteger()
                return True
            else:
                self.stack.append(iter(elem.getList()))
                
        return False# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())