"""
将不等概率的转换成的等概率的硬币，之后循环产生k次0-1，这些0-1的序列由先到后从低位到高位构成了组成n的二进制数
保留范围在1-n之内的结果就行
"""
# from Algorithm.SU_RandToEqualRand import RandToEqualRand
import random


def rand(p):
    return 1 if random.random() > (1-p) else 0


def RandToEqualRand(p):
    while True:
        a = rand(p)
        if a != rand(p):
            return a


def calc_k(n):
    k = 1
    while 2 ** k <= n:
        k += 1
    return k


def randTo1n0(p, n):
    k = calc_k(n)
    res = 0
    for i in range(k):
        res += RandToEqualRand(p) * 2**i
    if res > n or res == 0:  # 参考代码里面没有or res == 0，这样产生出来的结果有0
        res = randTo1n(p, n)
    return res



def randTo1n(p, n):
    k = calc_k(n)
    res = 0
    for i in range(k):
        if RandToEqualRand(p) == 1:
            res |= (1 << i)
    if res > n or res == 0:  # 参考代码里面没有or res == 0，这样产生出来的结果有0
        return randTo1n(p, n)
    return res


res = [randTo1n(0.7, 3) for _ in range(100000)]
from collections import Counter
for i, times in dict(Counter(res)).items():
    print(i, times, times/len(res))
print('-'*30)
res = [randTo1n0(0.7, 3) for _ in range(100000)]
from collections import Counter
for i, times in dict(Counter(res)).items():
    print(i, times, times/len(res))

# 3 33296 0.33296
# 2 33403 0.33403
# 1 33301 0.33301
# ------------------------------
# 2 33229 0.33229
# 1 33375 0.33375
# 3 33396 0.33396
