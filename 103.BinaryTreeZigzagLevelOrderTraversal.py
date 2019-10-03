# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res, levels, RightToLeft = [], [root], False
        # RightToLeft: tracks the order in curValues, odd level False, even level right
        # so odd level do ont perform reverse; even level perform reverse
        while levels:
            curValues, nextNodes = [], []
            for node in levels:
                curValues.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            if RightToLeft:
                curValues.reverse()
            if curValues:
                res.append(curValues)
            RightToLeft = not RightToLeft
            levels = nextNodes
        return res

