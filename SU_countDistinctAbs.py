class Solution:
    """ 题目描述是排序数组数组，二分查找，双指针 双指针是不是只能用在排序数组中 """
    def countDistinctAbs(self, nums):
        i, j = 0, len(nums) - 1
        cnt = 0
        while i < j:
            # # 新的i和j如果和之前处理过的相同的话就跳过，这是我的写法
            # 这是错误的，因为针对全相等的数组，第一次i和j进来的时候，
            # 没有之前处理过的i和j，此时为跳到下面判断nums[i]+nums[j]的语句块，
            # 相应的cnt会+1，然而在执行结束i=j的时候还会+1
            # 这样重复数组的返回结果成了2，正确答案是1

            # if i > 0 and nums[i] == nums[i - 1]:
            #     i += 1
            #     continue
            # if j < len(nums) - 1 and nums[j] == nums[j + 1]:
            #     j -= 1
            #     continue

            # 还有一种别人的写法是：
            # 表示：新的i和j如果和下一个没处理过的一样的话 就跳到下一个没处理过的位置
            # 和我的做法不一样的是，这个方法在第一次执行的时候就要确定这个数和下一个数会不会重复
            if j > 1 and nums[j] == nums[j - 1]:
                j -= 1
                continue
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
                continue

            if nums[i] + nums[j] == 0:
                i += 1
                j -= 1
            elif nums[i] + nums[j] > 0:  # 正数绝对值较大，或者全是正数，i和j都只能向绝对值减小的方向移动，哪个大就移动哪个
                j -= 1
            else:  # nums[i] + nums[j] < 0 负数绝对值大，应该将左指针向后移
                i += 1
            cnt += 1
        if i == j:
            cnt += 1
        return cnt


print(Solution().countDistinctAbs([3, 3, 3, 3, 3, 3, 3]))
print(Solution().countDistinctAbs([-3, -1, 0, 0, 2, 3, 5]))


