# n // 2, n % 2可以用位运算来提高速度
# n // 2  ==  n >> 1 (在返回是int值的情况下)
# n % 2 == n & 1

# n >> k 表示 n // 2^k
# n << k 表示 n * 2^k


class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = abs(n)
        result = 1
        while m:
            if m & 1 != 0:  # 奇数次幂，先在result上乘自己后转换成偶数次幂
                result *= x
            x *= x  # 将底数平方
            m >>= 1  # 将幂次数折半，直到为0
        return result if n > 0 else 1 / result


s = Solution()
print(s.myPow(3, 6))
