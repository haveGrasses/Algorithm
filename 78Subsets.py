class Solution:
    """ 基本的策略是每一次将下个数append到res列表中去，res先从空列表开始
    递归的思路：本次的结果等于上次的结果加上把本次传进来的nums中的每个数append上，
    每一次append的结果要进一步调用这个让其append的函数。。。晕了
    subset干的事：将nums中的数append到path中，append的结果再将该数之后的数append，以此类推
    """
    def __init__(self):
       self.res = []
    
    def subset(self, nums, path):
        self.res.append(path)
        for i in range(len(nums)):
            self.subset(nums[i+1:], path+[nums[i]])
        return self.res
    
    def subsets(self, nums):
        return self.subset(nums, [])

s = Solution()
print(s.subsets([4, 1, 2, 3, 2]))