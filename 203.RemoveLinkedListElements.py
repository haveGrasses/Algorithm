# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """ iteration method"""

    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':

        while (head != None) and (head.val == val):  # when head.val equals value to be removed, move head afterwards
            # delNode = head
            # head = head.next
            # delNode.next = None
            head = head.next  # move head afterwards

        if not head:  # after above operation, head == None means all values in LinkedList == val
            return head

        prev = head  # we can assure that prev.val ！= val after above two steps.
        while prev.next:  # if prev.next != None
            if prev.next.val == val:
                # delNode = prev.next
                # prev.next = delNode.next
                # delNode.next = None
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head


class Solution:
    """use dummy head to simplify code, avioding different operations between head and inner nodes"""

    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        dummyHead = ListNode(-1)  # assign a random value -1 to dummyHead,
        # the value does not matter because we would never access that value
        dummyHead.next = head

        prev = dummyHead  # now real head can be viewed as an inner node
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummyHead.next  # return real head


class Solution3:
    """use recursion"""
    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        # basic solution
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
