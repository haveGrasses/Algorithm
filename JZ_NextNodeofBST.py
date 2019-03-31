# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode.right:  # 如果存在右子树，找到右子树的最左边的结点
            pRight = pNode.right
            while pRight.left:  
                pRight = pRight.left
            pNext = pRight
        else:  # 不存在右子树需要向上找父节点 该父结点的right是当前节点
            pPar = pNode.next
            pCur = pNode
            if not pPar:
                return
            while pPar and pPar.right == pCur:
                pCur = pPar
                pPar = pPar.next
            pNext = pPar
        return pNext
    
