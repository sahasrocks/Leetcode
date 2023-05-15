class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length, curr = 1, head
        while curr:
            length += 1
            curr = curr.next
        length -= k
        v1, v2 = head, head
        while length > 1:
            length -= 1
            v1 = v1.next
        while k > 1:
            k -= 1
            v2 = v2.next
        v1.val, v2.val = v2.val, v1.val
        return head