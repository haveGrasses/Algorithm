# O(n^2)


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
        	for j in range(i + 1, len(nums)):
        		if nums[i] + nums[j] == target:
        			return i, j
        

# O(n)


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, x in enumerate(nums):
            a = target - x
            if a not in dict:
                dict[x] = i
            else:
                return [dict[a], i]

