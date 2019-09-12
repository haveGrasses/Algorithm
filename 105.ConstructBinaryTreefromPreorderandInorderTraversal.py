# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        indexMap = {}  # 记录inorde各个数对应的索引 实现inorder.index()方法
        for i in range(len(inorder)):
            indexMap[inorder[i]] = i
        root = self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, indexMap)
        return root

    def helper(self, preorder, preStart, preEnd, inorder, inStart, inEnd, indexMap):
        # 必须要check 不然preorder[preStart]会报index out of range错误
        # 原因是每次left那边preStart=preStart + 1，preEnd=preStart + length,当length=0时，preEnd是小于preStart的这时候
        # 如果不return的话，preStar会继续加，直到越界

        # 当然上面那个并不是写这个判断的核心原因，核心是什么时候是递归到底的情况，
        # 当length=0的时候，意味着左子树为空，此时root.left应该等于None

        if inStart > inEnd or preStart > preEnd:
            return None
        root = TreeNode(preorder[preStart])
        rootIndex = indexMap[root.val]
        length = rootIndex - inStart
        root.left = self.helper(preorder, preStart + 1, preStart + length, inorder, inStart, rootIndex - 1, indexMap)
        root.right = self.helper(preorder, preStart + length + 1, preEnd, inorder, rootIndex + 1, inEnd, indexMap)
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Solution().buildTree(preorder, inorder))
