from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        firstProfit = [0 for _ in range(len(prices))]
        cost = prices[0]
        for i in range(1, len(prices)):
            firstProfit[i] = max(firstProfit[i - 1], prices[i] - cost)
            cost = min(cost, prices[i])

        secondProfit = [0 for _ in range(len(prices))]
        # 在这里从后往前扫的时候，prices[i]变成了cost，之前的cost变成了sell price，所以这里变量名改成了maxSellPrice
        # 这个转变非常重要也非常妙
        maxSellPrice = prices[-1]
        # 为什么一定要从后往前扫呢:从后往前扫可以利用上一次算出来的profit更新下一次的，如果是从前往后扫，
        # 那上一次算出来的profit如果是第3天的，第4天的profit是不能用第3的，因为3不在4天之后的范围内，但是如果是第4天的profit，
        # 可以用来的更新第3天的profit，因为4天之后在3天之后的范围内
        for i in range(len(prices) - 2, -1, -1):  # range(len(prices)-2, 0, -1)也能AC，但是说不通啊 是要包含0的吧
            # 解释上面的问题：firstProfit[i]记录的是拿i作为卖出点的profit，在day[0, i]之内的收益
            # secondProfit[i]记录的是拿i作为买入点的profit，在day[i, n)之内的收益
            # 对于第0天，firstProfit[0]为0，secondProfit[0]为一次买卖的最大profit，如果不更新到0，secondProfit[0]恒为0，
            # 说明最值点永远不会在0点取得？NO，secondProfit[0]=firstProfit[n-1]，只要firstProfit[n-1]和secondProfit[0]
            # 有一个更新了就行，firstProfit[n-1] + secondProfit[n-1](=0) = firstProfit[0](=0) + secondProfit[0]，
            # eg, prices: [3,3,5,0,0,3,1,4]
            # firstProfit: [0, 0, 2, 2, 2, 3, 3, 4]
            # secondProfit: [4, 4, 4, 4, 4, 3, 3, 0]
            secondProfit[i] = max(secondProfit[i + 1], maxSellPrice - prices[i])
            maxSellPrice = max(maxSellPrice, prices[i])
        res = 0
        for i in range(len(firstProfit)):
            res = max(res, firstProfit[i] + secondProfit[i])
        return res


class Solution:
    """ no comments """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        firstProfit = [0 for _ in range(len(prices))]
        cost = prices[0]
        for i in range(1, len(prices)):
            firstProfit[i] = max(firstProfit[i - 1], prices[i] - cost)
            cost = min(cost, prices[i])

        secondProfit = [0 for _ in range(len(prices))]
        maxSellPrice = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            secondProfit[i] = max(secondProfit[i + 1], maxSellPrice - prices[i])
            maxSellPrice = max(maxSellPrice, prices[i])
        print(firstProfit)
        print(secondProfit)
        res = 0
        for i in range(len(firstProfit)):
            res = max(res, firstProfit[i] + secondProfit[i])
        return res


print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
