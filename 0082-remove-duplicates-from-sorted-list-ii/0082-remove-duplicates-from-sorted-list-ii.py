# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        cur=dummy
        while cur:
            if cur.next and cur.next.next and cur.next.val ==cur.next.next.val:
                temp=cur.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp=temp.next
                cur.next=temp.next
            else:
                cur=cur.next
        return dummy.next                
        
        
        # dummyNode=ListNode()
        # dummyNode.next=head
        # curr=dummyNode
        # while curr:
        #     if curr.next and curr.next.next and curr.next.val==curr.next.next.val:
        #         temp=curr.next.next
        #         while temp and temp.next and temp.val==temp.next.val:
        #             temp=temp.next
        #         curr.next=temp.next
        #     else:
        #         curr=curr.next
        # return dummyNode.next                





        # d=ListNode()
        # d.next = head
        # cur =d
        # while cur:
        #     if cur.next and cur.next.next and cur.next.val ==cur.next.next.val:
        #         temp=cur.next.next
        #         while temp and temp.next and temp.val ==temp.next.val:
        #             temp=temp.next
        #         cur.next=temp.next
        #     else:
        #         cur=cur.next
        # return d.next                