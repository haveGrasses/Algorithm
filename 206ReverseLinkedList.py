class Solution:
    """ 有点类似于反转字符串 """
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
