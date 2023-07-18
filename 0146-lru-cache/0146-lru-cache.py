class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        

class LRUCache:

    def __init__(self, capacity: int):
        """Initialize hash table & dll"""
        self.cpty = capacity
        self.htab = dict() #hash table 
        self.head = ListNode() #doubly linked list
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head 
        
    def _del(self, key: int) -> int: 
        """Delete given key from hash table & dll"""
        node = self.htab.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.val

    def _ins(self, key: int, value: int) -> None: 
        """Insert at tail"""
        node = ListNode(key, value, self.tail.prev, self.tail)
        self.tail.prev.next = self.tail.prev = node
        self.htab[key] = node
        
    def get(self, key: int) -> int:
        if key not in self.htab: return -1
        value = self._del(key)
        self._ins(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.htab: self._del(key)
        self._ins(key, value)
        if len(self.htab) > self.cpty: 
            self._del(self.head.next.key)
