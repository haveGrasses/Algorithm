class Solution:
    """ 这个解法看看就行，基本的策略是每一次将下个数append到res列表中去，res先从空列表开始
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


print(Solution().subsets([1,2,3,4]))


class Solution2:
    """ 更容易理解的iteration方法，并不推荐
    每for一次res的结果会变化一次，添加了新的元素
    因此下一侧的添加元素会再上一次结果的基础上加
    """
    def subsets(self, nums):
        res = [[]]
        for num in nums:  # another version：for num in sorted(nums)有什么用
            res += [r+[num] for r in res]  # 用列表推导式会快一些，改成循环memeroy limit error
        return res


print(Solution2().subsets([1, 2, 2]))


class Solution:
    """ 也不推荐，但是另外一个思路 """
    def subsets(self, nums):
        tmp=[]
        solution=[]
        level=0
        self.dfs(nums,tmp,solution,level)
        return solution

    def dfs(self,nums,tmp,solution,level):
        if level==len(nums):
            new_list = tmp.copy()
            solution.append(new_list)
            return
        # case 1: adding current element
        tmp.append(nums[level])
        self.dfs(nums,tmp,solution,level+1)
        # case 2: not adding current element
        tmp.remove(nums[level])
        self.dfs(nums,tmp,solution,level+1)


print(Solution().subsets([1,2,3]))


class Solution():
    """ 标准的回溯的写法 """
    def subsets(self, nums):
        res = []
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, index, path, res):
        res.append(path.copy())
        for i in range(index, len(nums)):
            path.append(nums[i])  # 实际上就是两种状态：要么加入num[i]
            self.backtrack(nums, i + 1, path, res)  # 注意这里是i+1，不是index+1，de了一晚上 + 0.2早上的bug
            # 主要是和permutations搞混了，permutations是index+1
            path.pop()  # 要么不加nums[i]


print(Solution().subsets([1, 2, 3]))

# permutations中的index的意思是，要填index位置的值，所以终止条件是当index == len(nums)说明全部位置填满
# subsets中的index的意思是，从第index位置开始逐一将之后的元素放进来，在index之前位置的元素不再考虑
