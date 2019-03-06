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
        slow.next = fast  # link slow anf fast
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
        
