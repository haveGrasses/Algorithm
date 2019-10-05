# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution0:
    """ bms """
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


class Solution:
    """ 差不多的思路 """
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        prev = dummyHead
        count = 0
        while count < m - 1:
            prev = prev.next
            count += 1
        # prev是前面保持不动的结尾

        tmp = prev.next  # 记录这个位置，这是反转后的结尾，要去接后面没反转的位置，相当于反转部分的head
        cur = prev.next
        start = None
        for _ in range(n - m + 1):
            nxt = cur.next
            cur.next = start
            start = cur
            cur = nxt
        prev.next = start  # start是反转部分反转后的头节点，prev是前面保持不动的结尾，连接起来
        tmp.next = cur  # tmp是反转部分反转后的尾节点，cur是后面没反转的头节点
        return dummyHead.next
