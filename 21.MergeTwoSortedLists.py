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
        """ 递归：先用if-else确定一个小的在前面，假如是l1，则l1.next=用同样的函数对l1.next 和 l2 进行处理，
        然后直接返回这一个条件中确定的最小的那个node，也就是l1！
        直接返回很重要，写这样的递归到后面很容易就会不知道最后到底要返回啥！以及在哪里返回！
        """
        if not l1 or not l2:
            return l1 or l2
        # 核心就是确定一个最小的在前面，后面的再递归获得，所以只要确定一个在前面的l就行，一个if-else搞定
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:  # l2.val <= l1.val
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists2(self, l1, l2):
        """ non-recursive: 初始一个dummyHead，初始一个cur从dummyHead开始，当l1和l2都不为空时，用if-else确定将
        谁加到cur的后面，加了之后后移相应对应链表的头，同时要后移cur到新加的节点上
        """
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


def data():
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

    # print(l1.toString())
    # print(l11.toString())
    return l1, l11


l1, l11 = data()
# print('l1: ', l1.toString(), 'l2: ', l11.toString())
print(Solution().mergeTwoLists(l1, l11).toString())
# print('l1: ', l1.toString(), 'l2: ', l11.toString())
# 上面这个函数会改变l1和l2的取值为：
# 1--> 2--> 3--> 4--> 4
# 1--> 1--> 2--> 3--> 4--> 4
l1, l11 = data()
print(Solution().mergeTwoLists2(l1, l11).toString())
