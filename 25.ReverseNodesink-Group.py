# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """ half bms, memo里有解释 """
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2 or not head or not head.next:  # 这个判断可以不要，主要是如果k=1，相当于一个一组反转，和原来一样的，直接返回，if not head 也可以由下面的while捕获到
            return head
        count = 0
        cur = head
        while cur and count < k:  # 看接下来是否够k个node
            cur = cur.next
            count += 1
        if count < k:
            return head

        prev, nxt = self.reverse(head, k)
        post = self.reverseKGroup(nxt, k)
        head.next = post  # 上两步可以合成 head.next = self.reverseKGroup(nxt, k)
        return prev

    def reverse(self, head, k):
        count = k
        prev, nxt = None, None
        cur = head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return prev, nxt


class Solution1:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2 or not head or not head.next:  # 这个判断可以不要，主要是如果k=1，相当于一个一组反转，和原来一样的，直接返回，if not head 也可以由下面的while捕获到
            return head
        count = 0
        cur = head
        while cur and count < k:  # 看接下来是否够k个node
            cur = cur.next
            count += 1
        if count < k:
            return head

        prev, nxt = self.reverse(head, count)  # 这里可以传k，然后在函数里面直接修改count，不用再在函数中另起一个count变量=k
        post = self.reverseKGroup(nxt, k)
        head.next = post  # 上两步可以合成 head.next = self.reverseKGroup(nxt, k)
        return prev

    def reverse(self, head, count):
        prev, nxt = None, None
        cur = head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return prev, nxt


class Solution2:
    """ 一道改编的题目：从结尾开始每k个一组反转：
    能想到的方法就是先找求出前面应该剩余多少个元素，然后从下一个节点开始正常的从前向后反转，也不需要判断是否够k个了，刚好够
    """
    def reverseKGroup_(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1
        if count != 0:
            skip = count % k
            if skip == 0:  # 可以用dummyHead处理
                return self.reverseKGroupHelper(head, k)
            cur = head
            while skip > 1:  # skip是前面剩下的元素的个数
                cur = cur.next
                skip -= 1
            # cur是前面不动的结尾
            cur.next = self.reverseKGroupHelper(cur.next, k)
        return head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """ dummyHead """
        dummyHead = ListNode(-1)
        dummyHead.next = head

        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1

        if count != 0:
            skip = count % k

            cur = dummyHead
            while skip > 0:  # skip是前面剩下的元素的个数
                cur = cur.next
                skip -= 1
            # cur是前面不动的结尾
            cur.next = self.reverseKGroupHelper(cur.next, k)
        return dummyHead.next

    def reverseKGroupHelper(self, head, k):
        if not head:
            return head
        prev, nxt = self.reverse(head, k)
        head.next = self.reverseKGroupHelper(nxt, k)
        return prev

    def reverse(self, head, k):
        count = k
        prev = None
        cur = head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return prev, cur


def constructLinkedList(nums):
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        cur.next = node
        cur = node
    return head


def printLinkedList(head):
    cur = head
    res = ''
    while cur:
        res += str(cur.val) + ' -> '
        cur = cur.next
    res += 'None'
    print(res)


head = constructLinkedList([1, 2, 3, 4, 5, 6, 7, 8])

print('Original List: ')
printLinkedList(head)

print('Reverse from left to right: ')
printLinkedList(Solution1().reverseKGroup(head, 3))

head = constructLinkedList([1, 2, 3, 4, 5, 6, 7, 8])
print('Reverse from right to left: ')
printLinkedList(Solution2().reverseKGroup(head, 3))

# 从后向前reverse可以的用lc oj来检验，先链表整个翻转，然后从后先前reverse，最后再整体翻转，得到的结果就是从前往后翻转的结果
print('Reverse from left to right using Solution2: ')
head = constructLinkedList([1, 2, 3, 4, 5, 6, 7, 8])
head = Solution2().reverseKGroup(head, 8)
head = Solution2().reverseKGroup(head, 3)
head = Solution2().reverseKGroup(head, 8)
printLinkedList(head)


class Solution3:
    """ 这是测试从后向前代码正确与否的 AC submission  """
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1
        if count != 0:
            head = self.reverseKGroup0(head, count, count)
            head = self.reverseKGroup0(head, k, count)
            head = self.reverseKGroup0(head, count, count)
        return head

    def reverseKGroup0_(self, head: ListNode, k: int, count) -> ListNode:
        """ 方法1 """
        skip = count % k
        if skip == 0:  # 可以用dummyHead处理这种情况，见下面的同名无下划线方法
            return self.reverseKGroupHelper(head, k)

        cur = head
        while skip > 1:  # skip是前面剩下的元素的个数
            cur = cur.next
            skip -= 1

        cur.next = self.reverseKGroupHelper(cur.next, k)
        return head


    def reverseKGroup0(self, head: ListNode, k: int, count) -> ListNode:
        """ 用dummyHead """
        skip = count % k
        dummyHead = ListNode(-1)
        dummyHead.next = head

        cur = dummyHead
        while skip > 0:  # skip是前面剩下的元素的个数
            cur = cur.next
            skip -= 1
        cur.next = self.reverseKGroupHelper(cur.next, k)
        return dummyHead.next

    def reverseKGroupHelper(self, head, k):
        if not head:
            return head
        prev, nxt = self.reverse(head, k)
        head.next = self.reverseKGroupHelper(nxt, k)
        return prev

    def reverse(self, head, k):
        count = k
        prev = None
        cur = head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return prev, cur


head = constructLinkedList([1, 2, 3, 4, 5, 6, 7, 8])
print('Reverse using Solution3: ')
printLinkedList(Solution3().reverseKGroup(head, 3))
