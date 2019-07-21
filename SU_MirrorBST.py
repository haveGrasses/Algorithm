"""
public static TreeNode mirrorTree1(TreeNode root)
    {
        if(root==null)
            return null;
        //对左右孩子镜像处理
        TreeNode left=mirrorTree1(root.left);

        TreeNode right=mirrorTree1(root.right);
        //对当前节点进行镜像处理。
        root.left=right;
        root.right=left;
        return root;
    }
"""


class Solution:
    def mirrorBST(self, root):
        if not root:
            return None
        # 处理左右孩子
        leftNode = self.mirrorBST(root.left)
        rightNode = self.mirrorBST(root.right)

        # 对当前节点进行处理
        root.left = rightNode
        root.right = leftNode
        return root
