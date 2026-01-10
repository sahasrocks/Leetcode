# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
        return slow    
        
        # a = []
        # while head:
        #     a.append(head)
        #     head = head.next
        # return a[len(a)//2]