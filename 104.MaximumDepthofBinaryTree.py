# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    def maxDepth2(self, root: TreeNode) -> int:
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
