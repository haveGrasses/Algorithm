# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        cur = dummyHead
        count = 0
        while count < m - 1:
            cur = cur.next
            count += 1
        # cur是前面保持不动的结尾
        cur.next, nxt, tail = self.reverse(cur.next, n - m + 1)
        tail.next = nxt
        return dummyHead.next

    def reverse(self, head, k):
        prev = None
        cur = head
        while k > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            k -= 1
        return prev, cur, head
