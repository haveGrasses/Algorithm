# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        
        while (head != None) and (head.val == val):
            delNode = head
            head = head.next
            delNode.next = None
        if head is None:
            return head
        
        prev = head  # we can assure that prev.val ！= val after above operations
        while prev.next:
            if prev.next.val == val:
                delNode = prev.next
                prev.next = delNode.next
                delNode.next = None
            else:
                prev = prev.next
        return head
