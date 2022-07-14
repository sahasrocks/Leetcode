# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=[]
        cur =head
        while cur:
            a.append(cur.val)
            cur=cur.next
        
        a.pop(-n)
              
        
        curr= dummy = ListNode(0)
        for e in a:
            curr.next= ListNode(e)
            curr= curr.next
        return dummy.next
    
        