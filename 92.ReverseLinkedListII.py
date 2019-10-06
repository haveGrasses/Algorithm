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


class Solution1:
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


class Solution2:
    """ 另一个思路：头插，从前往后的节点一个一个地插到prev后面
    prev: 没反转部分的尾节点，需要去接后面的结果
    tail: 反转部分的初始头节点，就是反转之后的尾节点，在循环过程中tail节点是一直不变的，但是其next是在不断变化的
    cur: tail.next，记录的是下一个要插到prev后面的节点
    front: prev.next，新的cur节点插过来需要将next指向front
    post: 未反转部分的头节点，反转后的尾节点要和post连起来
    """
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        prev = dummyHead
        for _ in range(m - 1):
            prev = prev.next

        tail = prev.next
        for _ in range(m-n):
            cur = tail.next
            post = cur.next
            front = prev.next

            prev.next = cur
            cur.next = front
            tail.next = post

        return dummyHead.next


class Solution3:
    """ Solution2的简化版，不用那么多变量存中间节点，像front永远是prev的next，就没必要存，post永远是cur.next，也没必要存 """
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head

        prev = dummyHead
        for _ in range(m-1):  # 循环次数m-1，走到需要反转的前一个节点
            prev = prev.next

        tail = prev.next
        for _ in range(n-m):  # 循环次数n-m，头插n-m个数
            cur = tail.next
            tail.next = cur.next
            cur.next = prev.next
            prev.next = cur

        return dummyHead.next


# Solution1 和 Solution2 都不错
