# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         a=[]
#         cur =head
#         while cur:
#             a.append(cur.val)
#             cur=cur.next
        
#         a.pop(-n)
              
        
#         curr= dummy = ListNode(0)
#         for e in a:
#             curr.next= ListNode(e)
#             curr= curr.next
#         return dummy.next
    
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        while n>0 and right:
            right=right.next
            n-=1
        while right:
            left=left.next
            right=right.next
        left.next=left.next.next
        return dummy.next        
        
        # dn=ListNode(0,head)
        # left=dn
        # right=head
        # while n>0 and right:
        #     right=right.next
        #     n-=1
        # while right:
        #     left=left.next
        #     right=right.next
        # left.next=left.next.next
        # return dn.next        
        # dummyNode=ListNode(0,head)
        # left=dummyNode
        # right=head
        # while n>0 and right:
        #     right=right.next
        #     n-=1
        # while right:
        #     left=left.next
        #     right=right.next
        # left.next=left.next.next
        # return dummyNode.next        
        
        
        
        
        
        # dummyNode=ListNode(0,head)
        # left=dummyNode
        # right=head
        # while n>0 and right:
        #     right=right.next
        #     n-=1
        # while right:
        #     left=left.next
        #     right=right.next
        # left.next=left.next.next
        # return dummyNode.next        
