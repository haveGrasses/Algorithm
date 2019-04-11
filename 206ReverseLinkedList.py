class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
