"""
TreeNode *getLastNode(TreeNode *root)
{
    if(root == NULL || root->left == NULL)    //递归出口，如果根为空，或者根为叶子节点。完全二叉树只需判定左儿子是否为空即可判定是否为叶子节点
        return root;

    int lh = 0;    //左子树高度
    TreeNode *ptn = root->left;
    while(ptn != NULL)
    {
        ++lh;
        ptn = ptn->left;
    }

    int rh = 0;　　//右子树高度
    ptn = root->right;
    while(ptn != NULL)
    {
        ++rh;
        ptn = ptn->left;
    }

    if(lh > rh)
        return getLastNode(root->left);
    else
        return getLastNode(root->right);
}

iterative：
TreeNode *getLastNode(TreeNode *root)
{
    if(root == NULL)
        return NULL;

    int height = 0;　　//先求树的高度
    TreeNode *ptn = root->left;
    while(ptn != NULL)
    {
        ++height;
        ptn = ptn->left;
    }

    TreeNode *last = root;
    while(last->left != NULL)　　//指向叶节点时退出
    {
        int lh = --height;　　　　//左子树的高度必然是父亲树高度-1

        int rh = 0;
        ptn = last->right;
        while(ptn != NULL)
        {
            ++rh;
            ptn = ptn->left;
        }

        if(lh > rh)
            last = last->left;
        else
            last = last->right;
    }

    return last;
}
"""


# 每次递归都下降一层，每次都求树的高度，时间复杂度为O(lgN * lgN)
class Solution:
    def getLastNode(self, root):
        if not root or not root.left:  # 空或者叶子节点
            return root
        leftHeight = 0  # 左子树高度
        next_node = root.left
        while next_node:
            leftHeight += 1
            next_node = next_node.left  # 都是左边

        rightHeight = 0  # 右子树的高度
        next_node = root.right
        while next_node:
            rightHeight += 1
            next_node = next_node.left  # 也是取决于左边的高度

        if leftHeight > rightHeight:  # leftHeight只有可能 >= rightHeight，并且相差最大为1
            # 左子树高度大于右子树高度说明最后一个叶子节点在左子树中，否则在右子树中
            return self.getLastNode(root.left)
        else:
            return self.getLastNode(root.right)
