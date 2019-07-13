class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            target = -1 * nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:  # num[start] + nums[end] == target
                    tmp = [nums[i], nums[start], nums[end]]
                    res.append(tmp)

                    # 避免重复是在append完之后进行了 第一次肯定不会有重复值，
                    # 所以这个逻辑没问题，在第一次append完之后
                    # 就要进行下面的这个过滤 过滤之后找到的答案一定是不同的
                    # 所以又可以放心地append

                    # avoid duplicates at 2nd ele
                    while start < end and nums[start + 1] == nums[start]:
                        start += 1
                    # avoid duplicates at 3rd ele
                    while start < end and nums[end - 1] == nums[end]:
                        end -= 1

                    start += 1
                    end -= 1
            i += 1
            # avoid duplicates at 1st ele
            while i < len(nums) - 1 and nums[i] == nums[i - 1]:
                i += 1
        return res
