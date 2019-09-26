class Solution:
    def permute(self, nums):
        if not nums or len(nums) == 0:
            return []
        self.ret = []
        self.used = [False] * len(nums)
        self.combination(nums, 0, [])
        return self.ret
    
    def combination(self, nums, index, path):
        if index == len(nums):
            self.ret.append(path.copy())  # 此处有坑，不能直接append(path)
            return
        for i in range(len(nums)):
            if not self.used[i]:  # 其实不需要这个dict，直接用if num i in path来判断这个数是否已经用过了，但是不够普适，比如又重复元素或者其他情况的时候，用dict是最普遍的方法
                path.append(nums[i])
                self.used[i] = True
                self.combination(nums, index+1, path)
                path.pop()
                self.used[i] = False
        return


class Solution2:
    def permute(self, nums):
        if not nums:
            return [[]]
        res = []
        used = [0] * len(nums)
        self.combination(nums, 0, [], used, res)
        return res

    def combination(self, nums, index, path, used, res):
        if index == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = 1
                self.combination(nums, index + 1, path, used, res)
                used[i] = 0
                path.pop()
        return


print(Solution2().permute([1,2,3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# >>> a = []
# >>> b = [1, 2, 3]
# >>> a.append(b)
# >>> a
# [[1, 2, 3]]
# >>> b.pop()
# 3
# >>> b
# [1, 2]
# >>> a
# [[1, 2]]
# >>>
