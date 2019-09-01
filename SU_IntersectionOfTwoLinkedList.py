class Solution(object):
    """不保证对"""
    def hasCycle(self, head):
        """返回的并不是入环节点，而是在环中的一个节点（slow和fast相遇的节点），不排除恰好是入环节点的情况"""
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def FirstIntersectNode(self, headA, headB):
        """关于如何定义交点在环内的第一个节点的：https://www.nowcoder.com/questionTerminal/db55f7f21127403cb268ffad9d23af37
        ：返回任意一个入环节点即可。
        首先找到来个链表的环中节点，兼容无环链表（环中节点为None），然后判断两个环是不是一个环，
        使用快慢指针判断在fast遇到slow之前是否遇到posB
        若不是同一个环返回None，若是同一个环，以任意一个pos为终点求两个五环链表相遇de第一个节点
        """
        posA, posB = self.hasCycle(headA), self.hasCycle(headB)
        if posA and posB:
            fast = posA.next.next  # 注1
            while fast != posA and (fast != posB and fast.next != posB):  # 注5
                fast = fast.next.next
                posA = posA.next
            if fast != posB or fast.next != posB:
                return None
            tmp1, tmp2 = headA, headB  # 注2
            len1, len2 = 0, 0
            while tmp1 != posB:
                len1 += 1
                tmp1 = tmp1.next
            while tmp2 != posB:
                len2 += 1
                tmp2 = tmp2.next
            diff = abs(len1 - len2)  # 注3
            tmp1, tmp2 = headA, headB
            if len1 > len2:
                while diff:
                    tmp1 = tmp1.next
                    diff -= 1
            if len2 > len1:
                while diff:
                    tmp2 = tmp2.next
                    diff -= 1  # 注4
            while tmp1 != posB and tmp2 != posB:
                tmp1 = tmp1.next
                tmp2 = tmp2.next
                if tmp1 == tmp2:
                    return tmp1
            return posB
        return None






# 注1：这里判断两个环是不是一个环的时候，只要从posA开始遍历，如果在回到posA之前遇到了和posB相等的节点
# 证明是同一个环，这样遍历的过程走的速度太慢
"""
tmp = posA.next
while tmp != posA and tmp != posB:
    tmp = tmp.next
if tmp != posB:
    return None
"""
# 可以采用快慢指针的方法，在fast遇到slow之前如果出现fast=posB或者fast.next=posB的，证明是同一个环
# fast走的速度比较快，有点一步并做两步走的感觉
"""
fast = posA.next.next
while fast != posA and (fast != posB or fast.next != posB):  # and后面这个条件其实是if break的条件
    fast = fast.next.next
    posA = posA.next
if fast != posB and fast.next != posB:
    return None
"""
# 注2：已经确定两个环是一样的环，现在要确定交点出现在环之前还是在环内，如果在环内，随便返回一个如环节点即可，注意是如环节点，
# 我们找到的posA和posB都不一定是如环节点，而是环中两指针相遇的节点

# 注3：其实这个解法是兼容了3中情况的解法 越想越觉得妙：当判断完是同一个环后，还是可能有两种情况，一是交点在环内，一是交点在
# 如环前面，此时以环内任意一个节点为终点，找第一个相同的节点就可以，这个方法找到的要么是如环前的交点，要么是
# 环的入口，满足条件

# 注4：当diff为0时，两个链表一样长，此时tmp1和tmp2不需要移动

# 注5：括号中是or还是and： not (fast == posB or fast.next == posB)：fast != posB and fast.next != posB
