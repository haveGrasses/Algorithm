class Solution(object):
    def majorityElement(self, nums):
        """
        Boyer-Moore Majority Vote Algorithm
        emmmmmmm, still a little bit confused
        :type nums: List[int]
        :rtype: int
        """
        
        cnt, major = 1, nums[0]  # Initially, the current candidate is set as major and the counter is 1.
        
        for i in range(1, len(nums)):
            if nums[i] == major:  # when current element equals major, increment counter
                cnt += 1
            elif cnt == 0:  # if counter is deduced to 0, it means that the recorded major may not be the real major 
            # unless it appears later again and do not be reduced to 0
            # caz if it is the major, then the times of it is > n // 2, so it won't be deduced to 0
                cnt += 1
                major = nums[i]
            else:
                cnt -= 1
        
        # if we can assure that the majority exists: then return major directly
        # the following step is only neccessary when there do not exits any major element
        
        cnt = 0
        for i in nums:
            if i == major:
                cnt += 1
        if cnt > len(nums) // 2:
            return major
        else:
            return 0
            


class Solution:
    """ JZ version """
    def MoreThanHalfNum_Solution(self, numbers):
        nums = numbers
        cnt, major = 1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] == major:
                cnt += 1
            elif cnt == 0:
                cnt += 1
                major = nums[i]
            else:
                cnt -= 1
        
        cnt = 0
        for i in nums:
            if i == major:
                cnt += 1
        
        if cnt > len(nums) // 2:
            return major
        else:
            return 0
