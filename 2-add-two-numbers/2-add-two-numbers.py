# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1n = []
        while l1:
            l1n.append(str(l1.val))
            l1 = l1.next
            
        l2n = []
        while l2:
            l2n.append(str(l2.val))
            l2 = l2.next
            
        s1 = int(''.join(l1n)[::-1])
        s2 = int(''.join(l2n)[::-1])
        
        s3 = str(s1+s2)[::-1]
        
        head = ListNode()
        tmp = head
        
        for i,s in enumerate(s3):
            
            if i == 0:
                tmp.val = int(s)
            else:
                x = ListNode(int(s))
                tmp.next = x
                tmp = tmp.next
                
        return head
        