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


class Solution2:
    """ 更容易理解的iteration方法 
    每for一次res的结果会变化一次，添加了新的元素
    因此下一侧的添加元素会再上一次结果的基础上加
    """
    def subsets(self, nums):
        res = [[]]
        for num in nums:  
            res += [r+[num] for r in res]  # 用列表推导式会快一些，改成循环memeroy limit error
        return res
