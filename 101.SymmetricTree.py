class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self.isSymmetricHlper(root.left, root.right)
        # 在根节点的时候只需要判断左孩子和右孩子，根节点自身的值不需要考虑，只需要看是否有值就行
    
    def isSymmetricHlper(self, left, right):
        if not left or not right:
            return left is right
        if left.val != right.val:
            return False
        
        return self.isSymmetricHlper(left.left, right.right) and \
               self.isSymmetricHlper(left.right, right.left)
               
