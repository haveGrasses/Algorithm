class Solution(object):

    def hasCycle(self, head):
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
        """
        cycleEntryA, cycleEntryB = self.hasCycle(headA), self.hasCycle(headB)
        if cycleEntryA and cycleEntryB:
            while cycleEntryA != cycleEntryB:
                cycleEntryA = cycleEntryA.next
            if cycleEntryA != cycleEntryB:
                return None
            # 确定了两个环是同样的环，接下来就是把环在内和外的情况一起考虑，以cycleEntryA为终点转换为两个无环链表相交的问题来做
            lenA, lenB = 0, 0
            tmp1, tmp2 = headA, headB
            while tmp1 != cycleEntryA:
                lenA += 1
                tmp1 = tmp1.next
            while tmp2 != cycleEntryA:
                lenB += 1
                tmp2 = tmp2.next
            diff = abs(lenA - lenB)
            tmp1, tmp2 = headA, headB
            if lenA > lenB:
                while diff:
                    tmp1 = tmp1.next
                    diff -= 1
            if lenB > lenA:
                while diff:
                    tmp2 = tmp2.next
                    diff -= 1
            while tmp1 != cycleEntryA and tmp2 != cycleEntryA:
                tmp1 = tmp1.next
                tmp2 = tmp2.next
                if tmp1 == tmp2:
                    return tmp1
            return cycleEntryA
            # 上面那个while的写法可不可以换成这个：
            # while tmp1 != tmp2:
            #     tmp1 = tmp1.next
            #     tmp2 = tmp2.next
            # if tmp1 != tmp2:
            #     return cycleEntryA
            # return tmp1
        return None
