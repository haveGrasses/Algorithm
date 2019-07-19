from typing import List


class Solution:
    """ dp"""
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cost, profit = prices[0], 0  # initialize, note profit = 0 for the first time 
        for i in range(len(prices)):
            cost = min(cost, prices[i])
            profit = max(profit, prices[i] - cost)
        return profit

