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
        return profit

