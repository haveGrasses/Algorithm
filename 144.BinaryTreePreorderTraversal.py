class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ 使用栈实现非递归 """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        if not root:
            return stack
        stack.append(root)
        
        while stack:
            curNode = stack.pop()
            res.append(curNode.val)
        
            if curNode.right:
                stack.append(curNode.right)
            if curNode.left:
                stack.append(curNode.left)
        return res


class Solution:
    """ 递归实现 """
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return self.res
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res

