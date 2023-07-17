# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        one =''
        two=''
        
        while l1:
            one+=str(l1.val)
            l1 = l1.next
        
        while l2:
            two+=str(l2.val)
            l2 = l2.next
        
        u= int(one)+int(two)
        s = ListNode(0)
        
        hea = s
        
        for i in str(u):
            s.next = ListNode(val =int(i))
            s = s.next
        return hea.next
        