from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ dfs """
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if root:
            self.search(root, '', res)
        return res

    def search(self, root, prefix, res):
        if not root.left and not root.right:
            res.append(prefix + str(root.val))
        if root.left:
            # 注意->是家在后面的，因为处死情况下prefix为空。不能是prefix +  '->' + str(root.val)
            self.search(root.left, prefix + str(root.val) +  '->', res)
        if root.right:
            self.search(root.right, prefix + str(root.val) + '->', res)
