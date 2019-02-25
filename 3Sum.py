class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) -2):
            # the if condition filters same number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            residual = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == residual:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # the following two while is very important, caz it aviods same answers
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] > residual:
                    r -= 1
                else:
                    l += 1
        return res
        

solution = Solution()
print(solution.threeSum([-2,0,0,2,2]))