# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        head = self.sortList(head)
        head2 = self.sortList(head2)
        return self.merge(head, head2)

    def merge(self, l1, l2):
        dummyHead = ListNode(-1)
        cur = dummyHead
        while l1 and l2:
            # merge
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            # cur.next = None
            pass
        if l1 or l2:
            cur.next = l1 or l2
        return dummyHead.next
