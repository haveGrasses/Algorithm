class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    """ 自己写的，有点一言难尽。。。
    反正思路就是用两个数组从两个节点向上回溯，记录路径，当两个节点在某时刻记录的路径的一样时，这个节点就是lca，之后可以不用再
    记录了，直接得到两个节点之间的path，但是path1和path2还是在继续向上记录，当然或许判断一下path如果非空，说明路径已经找到了
    不需要再记录了path1和path2了，，，
    总之这个代码就是很ugly，之前想的是把p和q的path1和path2通过两次调用SU_PathFromRootToOneNode的函数得到，之后
    找第一个相同的节点再组合起来，但是需要再去找一下两个数组的第一个相同的数，然后拼接，也不好...
    """
    def binaryTreePaths(self, root, p, q, path1, path2, path):
        found1, found2 = False, False
        if not root:  # 两个base condition
            return False, False, path
        if root.val == p:
            path1.append(root.val)
            return True, False, path
        if root.val == q:
            path2.append(root.val)
            return False, True, path
        if root.left:
            found1, found2, path = self.binaryTreePaths(root.left, p, q, path1, path2, path)
            if found1:
                path1.append(root.val)
            if found2:
                path2.append(root.val)
        if not found1 and not found2 and root.right:  # 左边没找到才会去右边找
            found1, found2, path = self.binaryTreePaths(root.right, p, q, path1, path2, path)
            if found1:
                path1.append(root.val)
            if found2:
                path2.append(root.val)
        elif found1 and root.right:
            _, found2, path = self.binaryTreePaths(root.right, p, q, path1, path2, path)
            if found2:
                path2.append(root.val)
        elif found2 and root.right:
            found1, _, path = self.binaryTreePaths(root.right, p, q, path1, path2, path)
            if found1:
                path1.append(root.val)

        if not path and path1 and path2 and path1[-1] == path2[-1]:  # path1[-1] == path2[-1]: lca found,not path： path已经找到了，不要再更新了，不然会把上层的节点也加上，比如9这种一定是相同路径下的节点，path1 and path2：两个节点找到的情况下path才有值
            # path = path1[:-1] + path2[::-1]  # 不能改变外面的path
            path.extend(path1[:-1] + path2[::-1])

        return found1, found2, path


class Solution2:
    """ 从根节点到目标节点的路径 错的 不想搞了"""
    def binaryTreePaths(self, root, p, q, path1, path2, path):
        found1, found2 = False, False
        if not root:
            return False, False, path

        path1.append(root.val)
        path2.append(root.val)

        if root.val == p:
            return True, False, path
        if root.val == q:
            return False, True, path

        if root.left:
            found1, found2, path = self.binaryTreePaths(root.left, p, q, path1, path2, path)

        if root.right:
            if not found1:
                found1, _, path = self.binaryTreePaths(root.right, p, q, path1, path2, path)
                path2.pop()
            if not found2:
                _, found2, path = self.binaryTreePaths(root.right, p, q, path1, path2, path)
                path1.pop()

        if not found1:
            path1.pop()
        if not found2:
            path2.pop()

        return found1, found2, path


class Solution3:
    """ 调两次从根节点到目标节点的路径函数，之后找公共祖先，再重组 """
    def binaryTreePath(self, root, p, path):
        """ 从叶子节点到跟节点的路径 """
        found = False
        if not root:
            return False
        if root.val == p:
            path.append(root.val)
            return True
        if root.left:
            found = self.binaryTreePath(root.left, p, path)
            if found:
                path.append(root.val)
                return True
        if not found and root.right:
            found = self.binaryTreePath(root.right, p, path)
            if found:
                path.append(root.val)
                return True
        if not found:
            return False

    def binaryTreePath2(self, root, p, path):
        """ 注意和上面的return的写法不同，这个写法更好，不用在每个if后面都去return，最后再去判断if not found: return False，
        想说return found 不就是return True if found else False的形式吗。。。要渐渐学习进步啊亲
        """
        found = False
        if not root:
            return False
        if root.val == p:
            path.append(root.val)
            return True
        if root.left:
            found = self.binaryTreePath2(root.left, p, path)
            if found:
                path.append(root.val)
        if not found and root.right:
            found = self.binaryTreePath2(root.right, p, path)
            if found:
                path.append(root.val)
        return found

    def binaryTreePath3(self, root, p, path):
        found = False
        if not root:
            return False
        path.append(root.val)
        if root.val == p:
            return True
        if root.left:
            found = self.binaryTreePath3(root.left, p, path)
        if not found and root.right:
            found = self.binaryTreePath3(root.right, p, path)
        if not found:
            path.pop()
        return found


    def extractPath(self, path1, path2, path):
        for i in range(len(path1)):
            start = 0
            while start < len(path2) and path1[i] != path2[start]:
                start += 1
            if start < len(path2) and path1[i] == path2[start]:
                path.extend(path1[:i]+path2[:start+1][::-1])
                return

    def nodeToNodePath(self, root, p, q):
        path1, path2, path = [], [], []
        self.binaryTreePath2(root, p, path1)
        self.binaryTreePath2(root, q, path2)
        self.extractPath(path1, path2, path)
        return path


class Solution4:
    """ 先找公共祖先，然后从祖先向下提取路径，走的长度会短一些，但是找祖先的过程有个dfs遍历，求路径又有两个dfs，未必比上面好 """

    def lca(self, root, p, q):
        """ 这里p和q是节点值，不是node类型 """
        if not root or root.val == p or root.val == q:
            return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def findPath(self, root, p, path):
        found = False
        if not root:
            return found
        path.append(root.val)
        if root.val == p:
            # found = True
            return found
        if root.left:
            found = self.findPath(root.left, p, path)
        if not found and root.right:
            found = self.findPath(root.right, p, path)
        if not found:
            path.pop()
        return found  # 注意这里一定要return回去，不然如果在左边找到了，上层函数才能找到found的值，不然上层found接住的是个None


    def nodeToNodePath(self, root, p, q):
        ancestor = self.lca(root, p, q)
        path1, path2 = [], []
        self.findPath(ancestor, p, path1)
        self.findPath(ancestor, q, path2)
        return path1[::-1][:-1] + path2


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

# print(getPath(root, root.right.left, root.right.right.left))
# 这里的root.right.left是不等于TreeNode(12)的，root.right.right.left是不等于TreeNode(20)的，即便值相等，左右孩子都是None
# 所以之后测试还是把这些节点一个个初始化后再用左右孩子连起来的好
path1, path2, path = [], [], []
Solution1().binaryTreePaths(root, 12, 20, path1, path2, path)
print(path1)
print(path2)
print(path)

# solution2是错的
# path1, path2, path = [], [], []
# Solution2().binaryTreePaths(root, 12, 20, path1, path2, path)
# print(path1)
# print(path2)
# print(path)

# path = []
# print(Solution3().binaryTreePath(root, 20, path))
# print(path)
#
# path = []
# print(Solution3().binaryTreePath3(root, 20, path))
# print(path)

path = Solution3().nodeToNodePath(root, 12, 20)
print(path)

path = Solution4().nodeToNodePath(root, 12, 20)
print(path)