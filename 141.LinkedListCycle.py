"""
class Solution {
public:
    bool hasCycle(ListNode *head) {

        if(head == NULL)
            return false;

        if(head->next == NULL)
            return false;

        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast != slow){
            if(fast->next == NULL)
                return false;
            if(fast->next->next == NULL)
                return false;

            fast = fast->next->next;
            slow = slow->next;
        }

        return true;
    }
};
"""
# 上面的代码有点复杂，因为return false的情况太多了，何不把return false
# 当作结束的return 在while里面只判断return True的情况

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

