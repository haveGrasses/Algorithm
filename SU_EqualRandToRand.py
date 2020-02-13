"""
只适用于产生1和0为0.7:0.3的非随机
"""
import random


def rand():
    return 1 if random.random() > 0.5 else 0


def calc_k(n):
    k = 1
    while not 2 ** k > n:
        k += 1
    return k


def generate_a(k):
    # a = rand() + rand() * 2**1 + rand() * 2**2 + rand() * 2**3 + rand()* 2**4
    a = 0
    for i in range(k):
        a += rand() * 2 ** i
    return a


def EqualRandToRand():
    k = calc_k(31)
    a = generate_a(k)
    if a >= 30:
        a = generate_a(k)  # a: 0~29, 30个数
    # 3 * 1 ~ 3 * 9 共9个能被3整除，返回0
    # 剩余30 - 9 = 21个不能被整除，返回1
    #  比例为9: 21 = 3:7
    if a != 0:  # 注意这个不等于0的情况，0%3=0，但0属于输出1的那一波
        if a % 3 == 0:
            return 0
    return 1


res = [EqualRandToRand() for _ in range(1000)]
print(sum(res) / len(res))  # 0.69
