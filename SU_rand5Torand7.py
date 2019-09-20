import random


def rand1ToM(m):
    """ 产生的是1-m的随机整数 """
    return int(random.random() * m + 1)


def MAry(n, m):
    """ 将n转化为m进制表示，注意带有前缀'0' """
    if n == 0:
        return '0'
    res = MAry(n // m, m)
    return res + str(n % m)


def randMAryLessN0(m, ary):
    res = ''
    index = 0
    equal = True
    while index != len(ary):
        res += str(rand1ToM(m) - 1)
        if equal:
            if res[index] > ary[index]:
                res = ''  # 如果不写这个一旦进入了这个if就会死循环了，
                # why：上次的res[index] > ary[index]没有被清空，还是一样的，必然满足条件，res无限制增加，但是index位置永远是>
                index = 0
                equal = True  # can not be commented
                continue
                # if下面几行相当于 return randMAryLessN(m, ary)，重新产生
            else:
                equal = res[index] == ary[index]
        index += 1
    if equal:
        return randMAryLessN(m, ary)  # 源码上有bug貌似，要用这一步筛掉等于n的数
    return res


def randMAryLessN(m, ary):
    res = ''
    index = 0
    previous_equal = True
    while index != len(ary):
        res += str(rand1ToM(m) - 1)  # 0-(m-1) 的数为m进制每一位的取值, TODO: 注意这里的str, 注意这里要减1
        if previous_equal:
            if res[index] > ary[index]:
                return randMAryLessN(m, ary)  # 还是直接递归调用简洁一点
            else:
                previous_equal = res[index] == ary[index]
        index += 1
    if previous_equal:
        return randMAryLessN(m, ary)  # 源码上有bug貌似，要用这一步筛掉等于n的数
    return res


def mAryToInt(ary, m):
    res = 0
    length = len(ary)
    for i in range(length):
        res += int(ary[i]) * m**(length-1-i)
    return res


def rand1ToN(n, m):
    n_m_ary = MAry(n, m)[1:]  # 将n转化为m进制表示, TODO: 注意这里的[1:]
    randOfMAry = randMAryLessN(m, n_m_ary)  # 产生一个小于n的m进制随机数，取值范围0-(n-1)
    return mAryToInt(randOfMAry, m) + 1  # 将m进制随机数变成十进制int，并将范围扩到1-n，TODO: 注意这里要+1


res = [rand1ToN(7, 5) for _ in range(100000)]
from collections import Counter
for i, j in dict(Counter(res)).items():
    print(i, j, j / len(res))


# ------------------------------- 一样的，命名不一样而已
def rand_1_to_m(m):
    return int(random.random() * m + 1)


def m_ary(n, m):
    if n == 0:
        return '0'
    res = m_ary(n // m, m)
    return res + str(n % m)


def rand_m_ary_less_n(ary, m):
    res = ''
    index = 0
    previous_equal = True

    while index < len(ary):
        res += str(rand_1_to_m(m) - 1)  # TODO: -1
        if previous_equal:
            if res[index] > ary[index]:
                return rand_m_ary_less_n(ary, m)
            else:
                previous_equal = res[index] == ary[index]
        index += 1

    if previous_equal:
        return rand_m_ary_less_n(ary, m)
    return res


def get_rand(m_ary_num, m):
    res = 0
    length = len(m_ary_num)
    for i in range(length):  # (length-1, -1, -1)
        res += int(m_ary_num[i]) * m ** (length-1-i)
    return res


def rand_1_to_n(m, n):
    n_m_ary = m_ary(n, m)[1:]
    rand_num_m_ary = rand_m_ary_less_n(n_m_ary, m)
    return get_rand(rand_num_m_ary, m) + 1


res = [rand_1_to_n(5, 7) for _ in range(100000)]
from collections import Counter
for i, j in dict(Counter(res)).items():
    print(i, j, j / len(res))
