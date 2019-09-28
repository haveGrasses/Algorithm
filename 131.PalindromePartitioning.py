class Solution:
    def partition(self, s: str):
        res = []
        self.dfs(s, 0, [], res)
        return res

    def isValid(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def dfs(self, s, index, path, res):
        if index == len(s):
            res.append(path.copy())
            return
        for i in range(index, len(s)):
            if not self.isValid(s, index, i):  # 注意这里的边界确定
                continue
            path.append(s[index: i + 1])
            self.dfs(s, i + 1, path, res)
            path.pop()


print(Solution().partition("aab"))
