class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ 和105如出一辙 """
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not inorder or not postorder:
            return None
        indexMap = {}
        for i in range(len(inorder)):
            indexMap[inorder[i]] = i
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, indexMap)

    def helper(self, inorder, inStart, inEnd, postorder, postStart, postEnd, indexMap):
        if inStart > inEnd or postStart > postEnd:
            return None
        root = TreeNode(postorder[postEnd])
        rootIndex = indexMap[root.val]
        length = rootIndex - inStart
        root.left = self.helper(inorder, inStart, rootIndex-1, postorder, postStart, postStart+length-1, indexMap)
        root.right = self.helper(inorder, rootIndex+1, inEnd, postorder, postStart+length, postEnd-1, indexMap)
        return root
