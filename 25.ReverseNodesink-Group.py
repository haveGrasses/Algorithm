# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """ half bms, memo里有解释 """
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2 or not head or not head.next:
            return head
        count = 0
        cur = head
        while cur and count < k:  # 看接下来是否够k个node
            cur = cur.next
            count += 1
        if count < k:
            return head

        prev, nxt = self.reverse(head, k)
        post = self.reverseKGroup(nxt, k)
        head.next = post  # 上两步可以合成 head.next = self.reverseKGroup(nxt, k)
        return prev

    def reverse(self, head, k):
        count = k
        prev, nxt = None, None
        cur = head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return prev, nxt
