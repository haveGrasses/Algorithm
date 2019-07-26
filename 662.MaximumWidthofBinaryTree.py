"""
We know that a binary tree can be represented by an array (assume the root begins from the position with
index 1 in the array). If the index of a node is i, the indices of its two children are 2*i and 2*i + 1.
The idea is to use two arrays (start[] and end[]) to record the the indices of the leftmost node and
rightmost node in each level, respectively. For each level of the tree, the width is end[level] - start[level] + 1.
Then, we just need to find the maximum width.


    public int widthOfBinaryTree(TreeNode root) {
        return dfs(root, 0, 1, new ArrayList<Integer>(), new ArrayList<Integer>());
    }

    public int dfs(TreeNode root, int level, int order, List<Integer> start, List<Integer> end){
        if(root == null)return 0;
        if(start.size() == level){
            start.add(order); end.add(order);
        }
        else end.set(level, order);
        int cur = end.get(level) - start.get(level) + 1;
        int left = dfs(root.left, level + 1, 2*order, start, end);
        int right = dfs(root.right, level + 1, 2*order + 1, start, end);
        return Math.max(cur, Math.max(left, right));
    }

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """ 如何求最大的宽度，就是通过找到最左和最右的节点来实现的，之前的想法是，把每层中的节点存到list中，然后计算list的length就可以了，
    相当与层序遍历的过程中同时计算每层的元素的个数，然后没到一层更新一下最大值。
    但是这个方法是，只记录每一层最左的节点和最右的节点，通过二叉树与数组的对应关系，只记录最左和最右的节点的索引（这一点很妙）
    这个方法的递归过程看得比较谜，因为这是一个有返回值的递归，这种递归就比较难。。。
    """
    def __init__(self):
        self.f = 0

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return self.dfs(root, level=0, order=1, start=[], end=[])

    def dfs(self, root, level, order, start, end):
        """
        :param root: node
        :param level: level
        :param order: current index, start from 1
        :param start: the indices of the leftmost node: indices相当于是在一个以数组形式存储的二叉树中的索引
        :param end: the indices of the rightmost node
        :return:
        """
        self.f += 1
        flag = '》'*self.f

        if not root:
            print(f'{flag} self.dfs({root.val if root else None}, level={level}, order={order}, start={start}, end={end})')
            return 0
        # 这对if和else是难点啊
        if len(start) == level:
            start.append(order)
            end.append(order)
        else:  # len(start) > level 说明在返回阶段了
            end[level] = order
        cur = end[level] - start[level] + 1

        print(f'{flag} self.dfs({root.val}, level={level}, order={order}, start={start}, end={end}), cur:{cur}')
        left = self.dfs(root.left, level+1, 2*order, start, end)
        self.f -= 1
        right = self.dfs(root.right, level+1, 2*order+1, start, end)
        self.f -= 1
        print(f'{flag} [recursion return to level {level}, node {root.val}], cur={cur}, left={left}, right={right}, return max({left}, {right}, {cur})={max(left, right, cur)}')

        return max(cur, left, right)


t1 = TreeNode(10)
t2 = TreeNode(5)
t3 = TreeNode(15)
t4 = TreeNode(2)
t5 = TreeNode(8)
t6 = TreeNode(14)
t7 = TreeNode(18)
t8 = TreeNode(1)
t9 = TreeNode(3)
t10 = TreeNode(6)
t11 = TreeNode(9)
t12 = TreeNode(20)
t1.left = t2
t1.right = t3

t2.left = t4
t2.right = t5

t3.left = t6
t3.right = t7

t4.left = t8
t4.right = t9

t5.left = t10
t5.right = t11

t7.right = t12

print(Solution().widthOfBinaryTree(t1))

