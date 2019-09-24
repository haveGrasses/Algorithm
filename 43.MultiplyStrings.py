class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        pos = [0 for _ in range(m + n)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[i])
                p1, p2 = i + j, i + j + 1
                total = mul + pos[p2]

                pos[p1] += total // 10
                pos[p2] = total % 10
        return ''.join(map(str, pos)) if pos else '0'

print(Solution().multiply('99', '99'))

class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                p1, p2 = i+j, i+j+1
                total = int(num1[i]) * int(num2[j]) + res[p2]
                res[p2] = total % 10  # 注意p2这里是等于，因为total里面已经加上p2原来的值了，现在要将p2大于10的部分分配到p1中
                res[p1] += total // 10
        # 一个自己写的不太好的处理开头为0的情况
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        if i == len(res) or len(res) == 0:
            return '0'
        return ''.join(map(str, res[i:]))


print(Solution2().multiply('0', '0'))


class Solution3:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                p1, p2 = i + j, i + j + 1
                total = int(num1[i]) * int(num2[j]) + res[p2]
                res[p2] = total % 10  # 注意p2这里是等于，因为total里面已经加上p2原来的值了，现在要将p2大于10的部分分配到p1中
                res[p1] += total // 10  # 当到最高位的时候这个结果肯定是小于10的，num1 * num2的结果的最大长度就是两个的长度和
        ret = ''
        for i in res:
            if not (len(ret) == 0 and i == 0):  # 注意这里是如何处理开头为0的情况的 if len(ret) != 0 or i != 0，真棒
                ret += str(i)
        return ret if ret else '0'


print(Solution3().multiply('0', '0'))
