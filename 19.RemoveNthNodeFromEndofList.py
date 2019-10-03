# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # add dummy head
        dummyHead = ListNode(-1)
        dummyHead.next = head
        slow = fast = dummyHead  # slow tracks the previous node of the node toi be deleted
        for _ in range(n):
            fast = fast.next  # make fast and low have a n-node's distance, so that when fast moves to the final node, low will be on the position of the preveious node of the node to be deleted
        while fast.next:  # moves fast to the final node
            fast = fast.next
            slow = slow.next
        # also we can get the node to be deleted if needed
        # deleted = slow.next
        slow.next = slow.next.next
        return dummyHead.next
        
