class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList0(self, head: ListNode) -> ListNode:
        """ 有点类似于反转字符串 """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

    def reverseList1(self, head: ListNode) -> ListNode:
        """ 不移动头节点的方法：
        prev：记录下一次要指向的节点
        cur：当前节点
        post：当前节点的下一个节点，因为当前节点需要指向prev，会丢失下一个节点，所以需要记录
        """
        prev = None
        cur = head
        while cur:
            post = cur.next
            cur.next = prev
            prev = cur
            cur = post
        return prev

    def reverseList(self, head: ListNode) -> ListNode:
        """ recursion """
        if not head or not head.next:  # base condition是 if not head.next, if not head 是为了整合了判断初始传入的head是否为空的情况
            return head
        ret = self.reverseList(head.next)  # 记录递归到底的节点返回用，每次递归完成一次就上传一次，到最后作返回用，实际上反转的过程是没有返回任何值的
        head.next.next = head
        head.next = None
        return ret
