from typing import List


# this ans is preferred
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            # the if condition filters same number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            residual = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == residual:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # the following two while is very important, caz it avoids same answers
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] > residual:  # 注1
                    r -= 1
                else:
                    l += 1
        return res


# 注1：为什么单独更新l和r的时候就不用去重了：因为上一次的值根本没被记录，如果这次和上次一样的值，但是另一个pointer会变，所以还是要保留


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
