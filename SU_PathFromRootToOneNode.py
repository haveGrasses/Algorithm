class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# SU_PathFromRootToOneNode1
class Solution1:
    """ 从目标节点到根节点的路径 """
    def binaryTreePaths(self, root, p, path):
        found = False
        if not root:  # 两个base condition
            return False
        if root.val == p:
            path.append(root.val)
            return True
        if root.left:
            found = self.binaryTreePaths(root.left, p, path)
            if found:
                path.append(root.val)
        if not found and root.right:  # 左边没找到才会去右边找
            found = self.binaryTreePaths(root.right, p, path)
            if found:
                path.append(root.val)
        return found


# SU_PathFromRootToOneNode
class Solution2:
    """ 从根节点到目标节点的路径 """
    def binaryTreePaths(self, root, p, path):
        found = False
        if not root:  # 两个base condition
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
        return found  # 注意这里一定要return回去，上层函数才能找到found的值，不然上层found接住的是个None


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

path = []
Solution1().binaryTreePaths(root, 20, path)
print(path)  # [20, 25, 15, 9]
