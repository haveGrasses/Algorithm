from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        firstProfit = [0 for _ in range(len(prices))]
        cost = prices[0]
        for i in range(1, len(prices)):
            firstProfit[i] = max(firstProfit[i-1], prices[i] - cost)
            cost = min(cost, prices[i])
        
        secondProfit = [0 for _ in range(len(prices))]
        # 在这里从后往前扫的时候，prices[i]变成了cost，之前的cost变成了sell price，所以这里变量名改成了maxSellPrice
        # 这个转变非常重要也非常妙
        maxSellPrice = prices[-1]
        for i in range(len(prices)-2, 0, -1):
            secondProfit[i] = max(secondProfit[i+1], maxSellPrice - prices[i])
            maxSellPrice = max(maxSellPrice, prices[i])  
            
        res = 0
        for i in range(len(firstProfit)):
            res = max(res, firstProfit[i] + secondProfit[i])
        
        return res

