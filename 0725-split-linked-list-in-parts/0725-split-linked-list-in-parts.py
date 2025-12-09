# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length,cur=0,head
        while cur:
            length+=1
            cur=cur.next
        base_len,rem=length//k, length%k
        cur=head
        res=[]
        for i in range(k):
            res.append(cur)
            for j in range(base_len - 1 + (1 if rem else 0)):
                if not cur:
                    break
                cur=cur.next
            rem -= (1 if rem else 0)
            if cur:
                cur.next,cur = None, cur.next
        return res                    
        