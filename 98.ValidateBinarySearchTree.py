class Solution:
    """ first version, a *wrong* answer 
    #         10
    #         / \
    #        5  15
    #           / \
    #          6  20
    # [10,5,15,null,null,6,20]
    
    上面这种情况是过不了的 原因是题目要求的是右子树的所有值都必须大于root结点的值
    显然第三层出现了6 是小于10的
    """
    def validate(self, root):
        if not root:
            return True
        
        if root.left and root.left.val >= root.val:
            return False
        
        if root.right and root.right.val <= root.val:
            return False
        
        
        return self.validate(root.left) and self.validate(root.right)
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root)

    
class Solution:
    def validate(self, root, lower, upper):
        if not root:
            return True
        
        # 当传入区间信息时，每次只需要关注该结点本身的值是否在区间内，不需要 check 左结点和右结点的大小
        # 左右结点是否合法会在下一次递归中确定，并且下一次已经传入了确定其是否合法的区间限制
        if root.val >= upper or root.val <= lower:
            return False
        
        return self.validate(root.left, lower, root.val) and \
               self.validate(root.right, root.val, upper)
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, -float('inf'), float('inf'))
