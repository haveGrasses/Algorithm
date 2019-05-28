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
