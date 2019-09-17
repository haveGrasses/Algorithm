"""
int Coin()  {
    while(true)  {
        int a = foo();
        if(a != foo()) {
            return a;
        }
    }
}
"""
import random


def rand(p):
    """ 构造一个不等概率的0-1产生器，以概率p产生1，概率1-p产生0 """
    return 1 if random.random() > (1-p) else 0


def RandToEqualRand0(p):
    """ 将以p为参数的不等概率产生器转化为等概率的产生器
    当a和b不等各取0或1时的概率是p*(1-p)，因此这两个事件是等概率事件，可以分别返回0，1
    其他两个事件互不等概率，因此出现时什么也不返回，需要重新调用函数
    """
    a = rand(p)
    b = rand(p)
    while a == b:  # 用while又是比较低级的写法
        a = rand(p)
        b = rand(p)
    if a == 1 and b == 0:
        return 1
    else:  # a == 0 and b == 1:
        return 0


def RandToEqualRand1(p):
    """ 实际上这也不是最优的 """
    a = rand(p)
    b = rand(p)
    if a == 1 and b == 0:
        return 1
    elif a == 0 and b == 1:
        return 0
    else:  # 当 a == b 时会重新调用该函数，直到满足上面条件之一返回，比while简洁很多
        return RandToEqualRand1(p)


def RandToEqualRand(p):
    """ preferred，没有必要再写一个if来看a和b是谁等于1，谁等于0，这两种情况等概率，随便挑一个return 1，另一个return 0就行
    所以这里选的是a是1就return 1，a是0就return 0，刚好用a这个变量把return的变化也表示出来了！妙～
    """
    while True:
        a = rand(p)
        if a != rand(p):
            return a


r1 = [rand(0.6) for _ in range(10000)]
print(sum(r1) / len(r1))
r2 = [RandToEqualRand(0.6) for _ in range(10000)]
print(sum(r2) / len(r2))
# 0.6001
# 0.5005
