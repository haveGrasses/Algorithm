# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        
        while (head != None) and (head.val == val):  # when head.val equals value to be removed, move head afterwards
            head = head.next  #  move head afterwards
            
        if head is None:  # after above operation, head == None means all values in LinkedList == val
            return head
        
        prev = head  # we can assure that prev.val ！= val after above two steps.
        while prev.next:  # if prev.next != None
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head
