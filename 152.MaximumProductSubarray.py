class Solution:
    """累乘最大，需要考虑正负的问题
    下一个数如果是正数，这个数最大的值是上一步的累乘乘以这个数与该数取最大
    下一个数是负数，该点最大的累乘应该是上一步最小的雷乘乘以该数与该数取较小
    因此每一步需要记录最大累乘和最小累乘
    """
    def maxProduct(self, nums: List[int]) -> int:
        maximun = big = samll = nums[0]  
        for i in range(1, len(nums)):
            if nums[i] < 0:  
            # 添加这一步判断可以避免big和samll计算后还要比较(big = max(big, samll)
                big, samll = samll, big  # negative one make samll bigger, make bigger samller
            big = max(nums[i], big*nums[i])
            samll = min(nums[i], samll*nums[i])
            maximun = max(maximun, big)  # 判断这一步计算过后是否得到比之前记录的最大值更大的结果
        return maximun
