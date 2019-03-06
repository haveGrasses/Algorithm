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
            return
        dummyHead = ListNode(0 if head.val != 0 else 1)
        slow, fast = dummyHead, head
        slow.next = fast
        while fast:
            while fast and fast.next and fast.val == fast.next.val:
                fast = fast.next
            if slow.next != fast:  # have repeated node
                slow.next = fast
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next
        return dummyHead.next
                
        
