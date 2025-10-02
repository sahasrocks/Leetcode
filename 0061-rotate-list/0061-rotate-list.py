# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length,tail=1,head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        if k==0:
            return head
        curr=head
        for i in range(length-k-1):
            curr=curr.next
        newHead=curr.next
        curr.next=None
        tail.next=head
        return newHead                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not head or not head.next:
        #     return head
        
        # old_tail = head
        # n = 1
        # while old_tail.next:
        #     old_tail = old_tail.next
        #     n += 1
        # old_tail.next = head
        
        # new_tail = head
        # for i in range(n - k % n - 1):
        #     new_tail = new_tail.next
        # new_head = new_tail.next
        
        # new_tail.next = None
        # return new_head
        