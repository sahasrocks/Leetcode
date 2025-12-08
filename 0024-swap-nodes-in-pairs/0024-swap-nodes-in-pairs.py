# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        while curr and curr.next:
            nxtPair=curr.next.next
            second = curr.next

            second.next=curr
            curr.next=nxtPair
            prev.next=second

            prev=curr
            curr=nxtPair
        return dummy.next    
        
        
        # def swap(node):
        #     if not node or not node.next:
        #         return node
        #     first, second = node, node.next
        #     first.next, second.next = second.next,first
        #     first.next = swap(first.next)
        #     return second
       
        # return swap(head)