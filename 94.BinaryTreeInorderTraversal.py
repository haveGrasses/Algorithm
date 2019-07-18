from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ recursive """

    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)

        return self.res


class Solution:
    """ non-recursive

    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 沿左孩子一直往下走 直到没有左孩子了
        cur, stack, res = root, [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            # 没有左孩子了，遍历当前节点
            cur = stack.pop()
            res.append(cur.val)
            # 当前节点遍历完，应该遍历其右子数，对右子树采取同样的方法，先走到最左边，再遍历最后一个，然后遍历右边
            cur = cur.right
        return res

