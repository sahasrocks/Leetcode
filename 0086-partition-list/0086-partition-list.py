# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left=ListNode()
        right=ListNode()
        ltail=left
        rtail=right
        while head:
            if head.val<x:
                ltail.next=head
                ltail=ltail.next
            else:
                rtail.next=head
                rtail=rtail.next
            head=head.next
        ltail.next=right.next
        rtail.next=None
        return left.next            
        
        
        
        
        
        
        
        
        
        
        
        # h1 = l1 = ListNode(0)
        # h2 = l2 = ListNode(0)
        
        # while head:
        #     if head.val < x:
        #         l1.next = head
        #         l1 = l1.next
        #     else:
        #         l2.next = head
        #         l2 = l2.next
        #     head = head.next
            
        # l2.next = None
        # l1.next = h2.next
        
        # return h1.next