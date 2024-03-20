# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tempA = tempB = list1

        while a>1:
            tempA=tempA.next
            a-=1
        
        while b>=0:
            tempB = tempB.next
            b-=1

        tempA.next = list2
        
        while tempA and tempA.next:
            tempA=tempA.next

        tempA.next = tempB

        return list1