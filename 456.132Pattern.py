class Solution:
    """ time: O(n^2) """
    def find132pattern(self, nums) -> bool:
        arr = nums.copy()
        for i in range(1, len(nums)):
            arr[i] = min(arr[i-1], nums[i-1])
        k_start = len(nums)
        for j in range(len(nums)-1, -1, -1):
            # 首先判断当前i和j是否满足条件
            if nums[j] == arr[j]:
                continue
            # i和j满足a[i] < a[j]
            # 现在要在j的右侧找到比a[i]大的最小值
            while k_start < len(nums) and arr[k_start] <= arr[j]:
                k_start += 1
            # i, j, k都有了，判断最后一个条件a[j] > a[k]是否满足
            if k_start < len(nums) and arr[k_start] < nums[j]:
                return True
            # 不满足则更新大于a[i]的最小值
            k_start -= 1
            arr[k_start] = nums[j]
        return False



class Solution:
    """ time: O(n), space: O(n) """
    def find132pattern(self, nums) -> bool:
        stack = []
        ak = -float('inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < ak:
                return True
            while stack and nums[i] > stack[-1]:
                ak = stack.pop()
            stack.append(nums[i])
        return False


# [1, 4, 2].
print(Solution().find132pattern([9, 11, 8, 9, 10, 7, 9]))



class Solution:
    """ time: O(n), space: O(1), an optimal solution """
    def find132pattern(self, nums) -> bool:
        """ nums的右半部分是递增的，严格的说是单调不减的 """
        ak = -float('inf')
        k = len(nums)
        for j in range(len(nums)-1, -1, -1):
            if nums[j] < ak:
                return True
            while k < len(nums) and nums[j] > nums[k]:  # 找到小于当前nums[j]的ak的最大值，以留给下一次check i最大的空间
                ak = nums[k]
                k += 1  # 相当于k pop出去了一个
            k -= 1
            nums[k] = nums[j]
        return False


nums = [9, 8, 9, 10, 11, 12, 13, 10, 7, 9]
print([i for i in range(len(nums))])
print(nums)
print(Solution().find132pattern(nums))
