from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ dfs """
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if root:
            self.search(root, '', res)
        return res

    def search(self, root, prefix, res):
        if not root.left and not root.right:
            res.append(prefix + str(root.val))
        if root.left:
            # 注意->是加在后面的，因为处死情况下prefix为空。不能是prefix +  '->' + str(root.val)
            self.search(root.left, prefix + str(root.val) +  '->', res)
        if root.right:
            self.search(root.right, prefix + str(root.val) + '->', res)


# SU_PathFromRootToOneNode
class Solution2:
    def binaryTreePaths(self, root, p, path):
        found = False
        if not root:
            return False
        path.append(root.val)
        if root.val == p:
            return True
        if root.left:
            found = self.binaryTreePaths(root.left, p, path)
        if not found and root.right:
            found = self.binaryTreePaths(root.right, p, path)
        if not found:
            path.pop()
        return found


# SU_ConstructBinaryTreefromLevelorderTraversal
def construct_tree(nums):
    root = TreeNode(nums.pop(0))
    queue = [root]

    while nums:
        cur = queue.pop(0)
        if cur:
            leftValue = nums.pop(0)
            cur.left = TreeNode(leftValue) if leftValue != -1 else None
            rightValue = nums.pop(0)
            cur.right = TreeNode(rightValue) if rightValue != -1 else None
            queue.append(cur.left)
            queue.append(cur.right)
        else:
            nums.pop(0)
            nums.pop(0)
    return root


root = construct_tree([9, 6, 15, 2, -1, 12, 25, -1, -1, -1, -1, -1, -1, 20, 37])

#                9
#          /          \
#       6               15
#     /                /   \
#   2                12     25
#                          /  \
#                         20   37

path = []
Solution2().binaryTreePaths(root, 20, path)
print(path)  # [9, 15, 25, 20]
