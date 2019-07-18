from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return res

