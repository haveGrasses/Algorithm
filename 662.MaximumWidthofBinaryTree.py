class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return self.dfs(root, level=0, order=1, start=[], end=[])
    
    def dfs(self, root, level, order, start, end):
        if not root:
            return 0
        
        if len(start) == level:
            start.append(order)
            end.append(order)
        else:
            end[level] = order
        
        curWidth = end[level] - start[level] + 1
        leftWidth = self.dfs(root.left, level+1, order*2, start, end)
        rightWidth = self.dfs(root.right, level+1, order*2+1, start, end)
        return max(curWidth, leftWidth, rightWidth)
