from typing import List


class Solution:
    """ 7.84% """
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i-1]
            if delta > 0:
                res += delta
        return res


class Solution:
    """ also 7.84 """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit, cost = 0, prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - cost)
            cost = min(cost, prices[i] - profit)
            # 只能进行一次买卖的时候，这里是：cost = min(cost, prices[i])
            # 而且profit先于cost更新，这两点都没懂
            # --0912更新，cost的计算解释：因为可以进行多次买卖，prices[i] - profit的意思是当前点的收益可以用来抵消当前点的成本，
            # 相当于在进行收益的累加
            # profit当然要先于cost更新。。。算当前收益的时候是在之前点的成本基础上算，当当前点算过之后，当前点需要参与成本计算为
            # 下一点计算收益做候选者
        return profit
