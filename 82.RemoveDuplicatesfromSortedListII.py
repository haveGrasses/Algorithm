# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummyHead = ListNode(0 if head.val != 0 else 1)  # avoid dummyHead same as head
        slow, fast = dummyHead, head  # slow tracks the node previous to repeated node
        # fast tracks node of the end of repeated node
        slow.next = fast  # link slow and fast
        while fast:  # every time fast moves afterwards
            while fast and fast.next and fast.val == fast.next.val:  # fast is not the end node and fast is repeated afterwards, so move fast to the next repeated node
                fast = fast.next
            if slow.next != fast:  # have repeat node between slow and fast
                slow.next = fast.next  # skip repeated element
                fast = slow.next  # move fast to the next node
            else:  # no repeated node, moves on both slow and fast
                slow = slow.next  # only remove continious repeatition, so slow and fast can moves on
                fast = fast.next
        return dummyHead.next
        

# ---------- from nc ----------- #

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return
        dummyHead = ListNode(0) if pHead.val != 0 else ListNode(1)
        dummyHead.next = pHead
        prev, cur = dummyHead, pHead
        while cur and cur.next:
            if cur.val == cur.next.val:
                tmp = cur.val
                # cur = cur.next
                while cur and cur.val == tmp:
                    cur = cur.next
                prev.next = cur
                # prev = prev.next  # caution: do not update prev in if loop, why:
                # if cur.val != tmp, we are not sure that if cur != cur.next, namely,
                # whether cur will be added to the return chain depends on the next while process, so it can not be add to prev.next
                # if in the next loop cur == cur.next, prev.next = cur will replace the current one,
                # so one word: ** prev.next is to be updated **
            else:
                prev.next = cur
                cur = cur.next
                prev = prev.next  # update prev only in else loop
                # caz if cur in else loop. it is certain that cur will be added to the return chain
        return dummyHead.next

