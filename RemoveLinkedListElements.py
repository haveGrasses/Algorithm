# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        
        while (head != None) and (head.val == val):
            head = head.next
            
        if head is None:
            return head
        
        prev = head  # we can assure that prev.val ！= val after above operations
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head
