class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        arr = self.nums.copy()

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        for i in range(len(arr) - 1, 0, -1):
            # p = random.randint(0, 10000) % (i+1)  # 产生[0, i)范围内的一个随机整数
            p = random.randrange(0, i + 1)
            swap(arr, i, p)
        return arr


import random
class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        ans = self.nums[:]                     # copy list
        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index
            ans[i], ans[j] = ans[j], ans[i]    # swap
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
