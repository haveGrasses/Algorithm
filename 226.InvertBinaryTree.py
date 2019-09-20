# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ self """
    def invertTree(self, root: TreeNode) -> TreeNode:
        """ recursion """
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """ iterative, 其实就是层序遍历 """
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
