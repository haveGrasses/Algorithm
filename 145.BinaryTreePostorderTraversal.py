from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ non-recursion
    和preorder思路一样，只需要再借助一个栈来实现反序就行！！！妙！
    后续遍历反序前序遍历是过程和结果都要反
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        output, res, stack = [], [], []
        stack.append(root)
        while stack:
            curNode = stack.pop()
            res.append(curNode.val)

            if curNode.left:  # 这里pre-order是先右后左
                stack.append(curNode.left)

            if curNode.right:
                stack.append(curNode.right)

        while res:
            output.append(res.pop())

        return output


class Solution:
    """ recursion """
    def __init__(self):
        self.res = []
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res

