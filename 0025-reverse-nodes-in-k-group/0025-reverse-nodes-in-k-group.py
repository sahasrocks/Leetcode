# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
#         dummy=ListNode(0,head) 
#         groupPrev=dummy

#         while True:
#             kth=self.getKth(groupPrev,k)
#             if not kth:
#                 break
#             groupNext=kth.next
#             prev,curr=kth.next,groupPrev.next
#             while curr !=groupNext:
#                 tmp=curr.next
#                 curr.next=prev
#                 prev=curr
#                 curr=tmp  
#             tmp=groupPrev.next
#             groupPrev.next=kth
#             groupPrev=tmp
#         return dummy.next    
#     def getKth(self,curr,k):
#             while curr and k>0:
#                 curr=curr.next
#                 k-=1
#             return curr
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if there are at least k nodes to reverse
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head   # not enough nodes → return as-is

        # Step 2: Reverse first k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Recurse for the rest of the list
        head.next = self.reverseKGroup(curr, k)

        # Step 4: prev is the new head of this reversed block
        return prev
