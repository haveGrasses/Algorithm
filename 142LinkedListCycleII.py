# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        phead = pHead
        if not phead or not phead.next:
            return 
        slow, fast = phead.next, phead.next.next
        if not slow or not fast:
            return
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        # fast meet slow
        fast = phead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    
# -------------- fix bug ----------------- #
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        phead = head
        if not phead or not phead.next:
            return 
        slow, fast = phead.next, phead.next.next
        if not slow or not fast:  
            return
        while slow != fast:
            if not fast or not fast.next:  # added
                return 
            slow = slow.next
            fast = fast.next.next
        # fast meet slow
        fast = phead
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
