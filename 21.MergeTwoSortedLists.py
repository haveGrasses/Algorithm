# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def toString(self):
        if not self:
            return ''
        res = f'{self.val}'
        l = self.next
        while l:
            res += f'--> {l.val}'
            l = l.next
        return res


# def toString(l):
#     if not l:
#         return ''
#     res = f'{l.val}'
#     l = l.next
#     while l:
#         res += f'--> {l.val}'
#         l = l.next
#     return res


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        # 核心就是确定一个最小的在前面，后面的再递归获得，所以只要确定一个在前面的l就行
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:  # l2.val <= l1.val
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists2(self, l1, l2):
        """ non-recursive """
        if not l1 or not l2:
            return l1 or l2
        dummyHead = ListNode(-1)
        cur = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummyHead.next


# 1 ->2->4, 1->3->4
l1 = ListNode(1)
l2 = ListNode(2)
l4 = ListNode(4)
l1.next = l2
l2.next = l4

l11 = ListNode(1)
l33 = ListNode(3)
l44 = ListNode(4)
l11.next = l33
l33.next = l44

print(l1.toString())
print(l11.toString())
print(Solution().mergeTwoLists(l1, l11).toString())
print('-----------')
print(l1.toString())
print(l11.toString())
# 1--> 2--> 4
# 1--> 3--> 4
# 上面的函数会改变l1和l2的取值
# 1--> 2--> 3--> 4--> 4
# 1--> 1--> 2--> 3--> 4--> 4

# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
# l44 = ListNode(4)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l44

# l11 = ListNode(1)
# l12 = ListNode(1)
# l22 = ListNode(2)
# l33 = ListNode(3)
# l444 = ListNode(4)
# l45 = ListNode(4)
# l11.next = l12
# l12.next = l22
# l22.next = l33
# l33.next = l444
# l444.next = l45
print(Solution().mergeTwoLists2(l1, l11).toString())

