# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        A, p = [], head
        while p:
            A.append(p.val)
            p = p.next
        n = len(A)
        return max([a+b for a,b in zip(A[:n//2], A[n//2:][::-1])])