# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2=headA,headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1    
        # curSet=set()
        # cur = headA
        # while cur:
        #     curSet.add(cur)
        #     cur=cur.next
        # cur=headB
        # while cur:
        #     if cur in curSet:
        #         return cur
        #     cur=cur.next
        # return None            
        
        
        
        
        # curA,curB = headA,headB
        # lenA,lenB = 0,0
        # while curA:
        #     lenA += 1
        #     curA = curA.next
        # while curB:
        #     lenB += 1
        #     curB = curB.next
        # curA,curB = headA,headB
        # for i in range(abs(lenA-lenB)):
        #     if lenA >= lenB:
        #         curA = curA.next
        #     else:
        #         curB = curB.next
        # while curB != curA:
        #     curA,curB = curA.next, curB.next
        # return curA