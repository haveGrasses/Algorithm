class Solution:
    def removeDuplicates(self, nums):
        id = 0  # initial res
        for n in nums:
            if id < 2 or n != nums[id-2]:
                # id < 2是针对前两个元素的，前两个元素总可以保留，
                # n != nums[id-2]是针对第三个起的之后元素的，要求其最多不能重复三次
                # （在有序情况下如果相等就重复三次了，不等说明最多重复了两次，也有可能一次都没有,符合条件）
                nums[id] = n
                id += 1
        return id


s = Solution()
print(s.removeDuplicates([1,1,2,2,3]))