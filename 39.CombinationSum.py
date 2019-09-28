class Solution:
    """ 自己写的，follow subset，permutation I 和 II 的思路 """
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, 0, [], res, target)
        return res

    def dfs(self, nums, index, path, res, target):
        if sum(path) > target:
            return

        if sum(path) == target:
            res.append(path.copy())
            return

        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i, path, res, target)
            path.pop()


print(Solution().combinationSum([2,3,6,7], 7))

# 几个backtrack的题的变化的地方：
# 1，往res中添加的条件：subsets是无条件添加，permutation是长度够了添加，combinationSum是和对了添加
# 2，减枝条件：combinationSum是和超过了就减, subsets没有，permutation是used就减
# 3，choice：permutation没有choice限制，循环space是一直是0到len(nums), subsets的条件是从index位置开始，中间调用的时候是i+1

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, 0, [], res, target)
        return res

    def dfs(self, nums, index, path, res, target):
        if target == 0:  # 思路其实是一样的，就是不用再算sum了
            res.append(path.copy())
        if target < 0:
            return
        for i in range(index, len(nums)):
            if target < nums[i]:  # 加这个判断，效率翻倍
                continue
            path.append(nums[i])
            self.dfs(nums, i, path, res, target - nums[i])
            path.pop()
