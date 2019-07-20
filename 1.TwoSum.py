# O(n^2)


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


# O(n)
class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for i, v in enumerate(nums):
            residual = target - v
            if residual not in hashMap:  # 判断residual在不在，增加的key是v
                hashMap[v] = i
            else:
                return hashMap[residual], i
