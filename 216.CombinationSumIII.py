class Solution:
    """ OMG, bms, 趁热打铁 """
    def combinationSum3(self, k: int, n: int):
        res = []
        self.dfs(k, 1, [], res, n)
        return res

    def dfs(self, k, index, path, res, n):
        if n == 0 and k == 0:
            res.append(path.copy())
            return

        for i in range(index, 10):
            if i > n:
                continue
            path.append(i)
            k -= 1
            self.dfs(k, i + 1, path, res, n - i)
            path.pop()
            k += 1


class Solution:
    """ 简洁版 """
    def combinationSum3(self, k: int, n: int):
        res = []
        self.dfs(k, 1, [], res, n)
        return res

    def dfs(self, k, index, path, res, n):
        if n == 0 and k == 0:
            res.append(path.copy())
            return

        for i in range(index, 10):
            if i > n:
                continue
            path.append(i)
            self.dfs(k - 1, i + 1, path, res, n - i)  # k-1和k+1就不要单独写了。。。
            path.pop()


class Solution:
    """ 一个条件判断优化,80~99.43% """
    def combinationSum3(self, k: int, n: int):
        res = []
        self.dfs(k, 1, [], res, n)
        return res

    def dfs(self, k, index, path, res, n):
        if n == 0 and k == 0:
            res.append(path.copy())
            return

        for i in range(index, 10):
            if (i * k + k * (k-1) / 2 > n):  # 由于不能重复，k个数，如果依次选下去，算最小的，都大于m那不用再看后面的了，放弃这条分枝
                continue
            path.append(i)
            self.dfs(k - 1, i + 1, path, res, n - i)
            path.pop()


class Solution:
    """ 优化+1：返回条件的优化，n !=0 而k=0的时候直接结束 """
    def combinationSum3(self, k: int, n: int):
        res = []
        self.dfs(k, 1, [], res, n)
        return res

    def dfs(self, k, index, path, res, n):
        if n == 0:  # 由 if n == 0 and k == 0 简化来的，因为k一定比n先达到0？
            res.append(path.copy())
            return
        if k == 0:
            return

        for i in range(index, 10):
            if (i * k + k * (k-1) / 2 > n):  # 由于不能重复，k个数，如果依次选下去，算最小的，都大于m那不用再看后面的了，放弃这条分枝
                continue
            path.append(i)
            self.dfs(k - 1, i + 1, path, res, n - i)
            path.pop()
