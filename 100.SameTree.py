# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 96%
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
        # 第二个函数是在判断第二个情况 （在p和q并非都有值的情况下他们什么时候会相等：都为None时）
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
    
    # compare 函数没有返回true的时候，如果没有返回false就继续比较下一个
    # 注意在compare里调的是isSameTree，而不是compare自己，因为compare
    # 自己没有对搜索到底的情况进行处理


# 一个更简介的方法：89%
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
        return p == q
        
  
