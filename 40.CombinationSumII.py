class Solution:
    """ 乘热打铁 bms """
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        used = [0] * len(candidates)
        self.dfs(candidates, 0, [], used, res, target)
        return res

    def dfs(self, nums, index, path, used, res, target):
        if target == 0:
            res.append(path.copy())
            return
        if target < 0:  # 现在内部判断了if target < nums[i]的情况下这个可以不要了
            return
        for i in range(index, len(nums)):
            if target < nums[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            path.append(nums[i])
            used[i] = 1
            self.dfs(nums, i + 1, path, used, res, target - nums[i])
            path.pop()
            used[i] = 0


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.dfs(candidates, 0, [], res, target)
        return res

    def dfs(self, nums, index, path, res, target):
        if target == 0:
            res.append(path.copy())
            return
        for i in range(index, len(nums)):
            if target < nums[i] or (i > index and nums[i] == nums[i - 1]):  # 再次出现容易犯的错误：是 i > index 而不是 i > 0
                # 之前每发现这个错误还多去使用了个used, 实际上不用
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res, target - nums[i])
            path.pop()


# 总结一下，好像只有permutations里面会使用used，subset和combinationSum的题都不用
