# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow == fast:
                break
        else:
            return None
        while head !=slow:
            head,slow=head.next,slow.next
        return head                
        
        # slow,fast=head,head
        # while fast and fast.next:
        #     fast=fast.next.next
        #     slow=slow.next
        #     if slow == fast:
        #         break
        # else:
        #     return None
        # while head != slow:
        #     head,slow = head.next,slow.next
        # return head                
        
        # slow,fast=head,head
        # while fast and fast.next:
        #     fast=fast.next.next
        #     slow=slow.next
        #     if slow==fast:
        #         break
        # else:
        #     return None
        # while head != slow:
        #     head,slow=head.next,slow.next
        # return head                


       
       
        # Initialize pointers at head of linkedlist...
        # p1 = p2 = head
        # # Run a loop until p2 and p2.next is equal to null...
        # while p2 and p2.next:
        #     # Moving p1 by 1 & p2 by 2
        #     p1, p2 = p1.next, p2.next.next
        #     # found the cycle...
        #     if p1 == p2: break
        # # In case there is no cycle or no meeting point...
        # else: return None
        # # run loop until again head & p1 don't collab...
        # while head != p1:
        #     # Moving head by 1 & p1 by 1 as well...
        #     head, p1 = head.next, p1.next
        # return head 
        