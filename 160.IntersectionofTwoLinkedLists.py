class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # has cycle
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        endofA = headA
        while endofA.next:
            endofA = endofA.next
        endofA.next = headB
        ret = self.hasCycle(headA)
        endofA.next = None
        return ret
