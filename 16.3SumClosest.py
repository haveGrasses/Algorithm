class Solution:
    def threeSumClosest(self, nums, target):
        closet = nums[0] + nums[1] + nums[2]  # initialize beat ans
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == target:
                    return curSum
                if abs(curSum - target) < abs(closet - target):  # attention:abs
                    closet = curSum
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return closet

s = Solution()
print(s.threeSumClosest([1,1,1,0], -100))