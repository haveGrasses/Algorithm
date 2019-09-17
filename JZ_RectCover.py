class Solution:
    """ 这里的覆盖方法仅仅指的是横着覆盖还是竖着覆盖，不是说哪个矩形放在不同的位置都算一种不同的覆盖方法
    当横着放的时候，下侧一定是横着放的，不加方法，右侧是子问题
    """
    def rectCover(self, number):
        if number <= 1:
            return number
        dp1, dp2 = 1, 1
        for i in range(2, number+1):
            dp1, dp2 = dp2, dp1 + dp2
        return dp2


print(Solution().rectCover(2))
