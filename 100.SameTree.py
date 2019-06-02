# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return self.compare(p, q)
        return p == q  # 妙！
        
        # 当 if p and q 为False的时候，有三种情况
        # - p为None，q非None
        # - q为None，p非None
        # - p为None，q为None
        # 只有最后一种情况会返回True
        # 总结一下：返回True的情况有两种：一种是p和q都不为None，且他们的值相等
        # 二是p和q同时为None
        # 所以这个函数里面第一个return就是在判断第一种情况
        # 第二个函数是在判断第二个情况
        # 第二个return相当于
        # if p is None and q is None:
        #     return True
        # else:
        #     return False
    
    def compare(self, p, q):
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
