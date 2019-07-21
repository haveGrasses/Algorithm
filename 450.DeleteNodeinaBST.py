class Soution:
    """ 未经检验 """
    def minimum(self, root):
        if not root.left:
            return root
        return self.minimum(root.left)

    def removeMin(self, root):
        if not root.left:
            rightNode = root.right
            root.right = None
            return rightNode
        root.left = self.removeMin(root.left)
        return root

    def remove(self, root, e):
        if not root:
            return None
        if e < root.left:
            root.left = self.remove(root.left, e)
            return root
        elif e > root.val:
            root.right = self.remove(root.right, e)
            return root
        else:  # root.val == e
            # left child is null
            if not root.left:
                rightNode = root.right
                root.right = None
                return rightNode

            # right child is null
            if not root.right:
                leftNode = root.left
                root.left = None
                return leftNode

            # neither left nor right node is null
            successor = self.minimum(root.right)
            successor.right = self.removeMin(root.right)
            successor.left = root.left

            root.left = root.right = None
            return successor


