class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0 | length == 1:
            return length

        k = 0
        while k < length - 1 and nums[k] == nums[k+1]:
            k += 1
        result = 2
        samllReq = nums[k] < nums[k+1]
        for i in range(k+1, length-1):
            if samllReq and nums[i+1] < nums[i]:
                nums[result] = nums[i+1]
                result += 1
                samllReq = ~samllReq
            elif ~samllReq and nums[i+1] > nums[i]:
                nums[result] = nums[i+1]
                result += 1
                samllReq = ~samllReq
        print(nums)
        return result


class Solution2(object):
    """ beats 100%, use dp"""
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1  # still do not understand why up just equals previous down plus 1
            elif nums[i] < nums[i-1]:
                down = up + 1  # same confusion
        return max(up, down)    
    

s = Solution()
print(s.wiggleMaxLength([2, 1, 4, 5, 6, 3, 3, 4, 8, 4]))
