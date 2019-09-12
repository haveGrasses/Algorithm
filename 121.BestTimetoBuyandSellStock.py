from typing import List


class Solution:
    """ dp
    profit: 如果在该点卖出所能达到的最大收益
    得到这个最大收益，需要知道在当前该点的最小cost
    profit 本来是一个一维数组，记录的是每个点的最大收益，相应地需要知道该点之前的最小cost，所以需要记录这个cost
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cost, profit = prices[0], 0  # initialize, note profit = 0 for the first time
        for i in range(len(prices)):
            profit = max(profit, prices[i] - cost)  # 这里的cost是i点之前的最小cost
            cost = min(cost, prices[i])  # 在更新完profit后更新cost，把当前点考虑进来
        return profit


# 看一下最原始的暴力解法，结果当然是LTE，但是有必要对比想一下是如何优化为dp的思路的：
# 没有必要让每个点都成为买入点，只需要记录该点之前的最优的买入点就行，因此引入cost，这样就消去了外层的while
# 只需要循环prices，找最佳的卖出点就行
class Solution1:
    """轮流让每个点成为买入点，依次计算该点之后的每个点买入的profit"""
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0
        while buy < len(prices):
            for sell in range(buy, len(prices)):
                res = max(res, prices[sell] - prices[buy])
            buy += 1
        return res
