class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        """ 有点类似于反转字符串 """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

    def reverseList(self, head: ListNode) -> ListNode:
        """ 递归 """
        pass

