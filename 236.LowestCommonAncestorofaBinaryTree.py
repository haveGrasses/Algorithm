# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        二叉树的后续遍历的过程就是先处理左子树，再处理右子树，最后处理根节点的过程
        先序遍历就是先处理根节点，再处理左子树，最后处理右子树的过程
        中序遍历是先处理左子树，再处理根节点，最后处理右子树的过程，
        这里使用的是后序遍历 为啥 因为要先看两个子树
        思路：
        看当前节点是否满足条件，满足则return，为空也return，不再去看左右子树了
        否则先后得到左子树和右子树的返回结果
        如果两个都不为空则返回当前节点，谋则返回不为空的那个，都为空时返回空

        """
        # 每次return的要么是自己子树中找到的给定节点，要么就是最近公共节点，如果有一次return的是公共节点，则继续往上的过程中return
        # 的都是这个公共节点
        if root is None or root == p or root == q:  # 决定要不要后序遍历
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right


class Solution2:
    """数组的形式"""

    def lowestCommonAncestor(self, nums, p, q):
        return self.helper(nums, 0, len(nums) - 1, p, q)

    def helper(self, nums, start, end, p, q):
        if start >= len(nums) or nums[start] == -1 or nums[start] == p or nums[start] == q:
            return nums[start] if start < len(nums) else -1
        left = self.helper(nums, 2 * start + 1, end, p, q)
        right = self.helper(nums, 2 * start + 2, end, p, q)

        if left != -1 and right != -1:
            return nums[start]
        return left if left != -1 else right


print(Solution2().lowestCommonAncestor([9, 6, 15, 2, -1, 12, 25, -1, -1, -1, -1, -1, -1, 20, 37], 12, 20))
