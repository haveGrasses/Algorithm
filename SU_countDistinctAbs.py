class Solution:
    def countDistinctAbs(self, nums):
        i, j = 0, len(nums) - 1
        cnt = 0
        while i < j:
            # 去掉重复元素
            if j > 1 and nums[j] == nums[j - 1]:
                j -= 1
                continue
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
                continue
            if nums[j] + nums[i] > 0:  # 正数的绝对值较大
                j -= 1
            elif nums[j] + nums[i] < 0:  # 负数的绝对值较大
                i += 1
            else:  # 绝对值相等
                j -= 1
                i += 1
            cnt += 1  # 除了两个continue的情况不需要不需要加cnt外，其余不管怎么动，都要加cnt，也可以把这个cnt写到每个if和else里
        if i == j:  # 如果所有的值都相等，记录最后一个，如果不是都相等，也需要记录最后一次走到的这个元素
            cnt += 1
        return cnt


print(Solution().countDistinctAbs([3, 3, 3, 3, 3, 3, 3]))
print(Solution().countDistinctAbs([-3, -1, 0, 0, 2, 3, 5]))
