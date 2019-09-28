class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        used = [0] * len(nums)
        self.dfs(nums, 0, [], used, res)
        return res

    def dfs(self, nums, index, path, used, res):
        if index == len(nums):
            res.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            # 就这个条件，想了一个小时没想出来，自己写的是if used[i] or (i > 0 and nums[i] == nums[i-1]) 不对，
            # if (used[i] | | i > 0 & & nums[i] == nums[i - 1] & & !used[i - 1]) continue;

            # 需要加and not used[i-1]，表示的是如果当前数和前一个数重复了，但是前一个数已经在path中了就还是可以选这个数
            # 但是如果当前数和前一个数重复了，而且前一个数也没有用，就不能选当前数
            # 前一个数没有用的意思其实前一个数已经选择过了，并且返回了最终的path，不然前一个数肯定是used锁定了的
            # 故前一个数的used为0表示的是前一个数已经尝试完所有的选择情况了，这次的数和它一样的话就不要再选了

            path.append(nums[i])
            used[i] = 1
            self.dfs(nums, index + 1, path, used, res)
            path.pop()
            used[i] = 0


print(Solution().permuteUnique([1, 1, 2]))
# [[1,1,2],[1,2,1],[2,1,1]]
