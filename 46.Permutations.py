class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
            if not self.used[i]:
                path.append(nums[i])
                self.used[i] = True
                self.combination(nums, index+1, path)
                path.pop()
                self.used[i] = False
        return
    
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
