class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead1(self, listNode):
        """先反转链表，再顺序add到res"""
        prev = None
        while listNode:
            cur = listNode
            listNode = listNode.next
            cur.next = prev
            prev = cur
        # prev是反转后的头节点
        res = []
        while prev.next:
            res.append(prev.val)
            prev = prev.next
        return res

    def printListFromTailToHead(self, listNode):
        """递归"""
        res = []
        return self.add(listNode, res)

    def add(self, listNode, res):
        if not listNode:
            return res
        self.add(listNode.next, res)
        res.append(listNode.val)
        return res
