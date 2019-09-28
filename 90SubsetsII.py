class Solution0:
    """与非重复迭代的思路一样 emmmmmmm 不推荐这个方法
    如何处理重复元素：先排序（排序是为了能够用nums[i] == nums[i-1]来判断重复元素）
    非重复元素需要的话res中的所有结果都要append上这个数
    重复元素则再上一次append的基础进一步append，不会再让res中的所有元素都去append这个数
    因为这个数和上一个数相同，而上一个数已经append了
    """    
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        res, curr = [[]], []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # 和上一个数重复了
                curr = [r + [nums[i]] for r in curr]  # 推导式中的curr是上一次的结果
            else:
                curr = [r + [nums[i]] for r in res]
            res += curr
        return res


class Solution:
    """ dfs """
    def subsetsWithDup(self, nums):
        nums.sort()  # 排序的作用是一样的，为了用nums[i] == nums[i - 1]来去掉重复元素
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path.copy())
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()
