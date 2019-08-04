# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """无序链表的排序常见的做法是mergesort，merge的部分其实就是21. Merge Two Sorted Lists合并两个有序链表,
    现在核心是完成sort那一部分，sort用slow，fast两个指针把head分成差不多均等的两部分，然后对这两部分再调用sortList函数，
    最后merge，利用
    """

    def sortList(self, head: ListNode) -> ListNode:
        """这道题有个要求是O(1)的space，但是这个递归的方法是O(nlogn)的space,
        虽然递归函数本身是O(1)的space，有实现的O(1)的版本，需要用到栈貌似，没看
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None  # 将链表从slow所在的位置断开成两个链表head和head2, slow所在的位置大致为原head的中间位置，
        # 这样就将原head分成了长度大致相等的head和head1，当原head长度为奇数时，head比head1多一个元素
        # 再对head和head2进行排序
        head = self.sortList(head)
        head2 = self.sortList(head2)
        return self.merge(head, head2)

    def merge(self, l1, l2):
        dummyHead = ListNode(-1)
        cur = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            # cur.next = None  # 严格来说需要这样，现在cur.next带的是l1或l2的next，不过下次会覆盖掉这个值
        if l1 or l2:
            cur.next = l1 or l2
        return dummyHead.next
