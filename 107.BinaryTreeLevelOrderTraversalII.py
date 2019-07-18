from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ 和levelorder一样，只需要res[::-1]把结果反序一下就行了"""
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], []
        queue.append(root)
        while queue:
            cnt = len(queue)
            tmp = []
            while cnt:
                cur = queue.pop(0)
                tmp.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    
                cnt -= 1
            res.append(tmp)
        return res[::-1]
 
