"""
# SU_MinMaxInBinarySearchTree
二分搜索树中查找比target大的最小值
```
public Integer find1(Node node, int target){
    if(node == null)return null
    if(node.data <= target){  //查找大的，要去右边找
       return find1(node.right, target)
    } else {  // root已经比target大了，去左边找最小的
        Integer x= find1(node.left, target)
        return (x == null) ? node.data : x
    }
}
```

二分搜索树中查找比target小的最大值
```
public Integer find2(Node node, int target){
    if(node == null)return null
    if(node.data >= target){
        return find2(node.left, target)
    } else {
        Integer x= find2(node.right, target)
        return (x == null) ? node.data : x
    }
}
```
#%%

"""
class Solution:
    def findMinofGreater(self, root, target):
        if not root:
            return None
        if root.val <= target:  # 根结点小于等于目标值，去右子树中找大于目标值的节点
            return self.findMinofGreater(root.right, target)
        else:  # 根结点大于目标值，去左子树找最小的元素
            x = self.findMinofGreater(root.left, target)
            # 这里去左边找最小的元素时候，只有当左节点的值大于目标值时才会继续向左找满足大于情况下更小的，
            # 当左节点的值小的时候会去右边找 直到某一次的向下找的过程中没有节点了
            # 如果是从右节点返回的 说明进入的条件是root.val <= target，即没有在左边找到大于target的节点
            # 直接return None 返回给初始进入有节点的那个左节点的函数，此时x为None，下一步取root节点的值
            # 有点迷...
            return x if x else root.val

    def findMaxofLesser(self, root, target):
        if not root:
            return None
        if root.val >= target:  # 根节点值大于等于目标值，去左节点找小于目标值的节点
            return self.findMaxofLesser(root.left, target)
        else:  # 根节点小于目标值，去右节点找最大的
            x = self.findMaxofLesser(root.right, target)
            return x if x else root.val
