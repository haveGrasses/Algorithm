"""
recursion：
base condition：n == 0: return '0'
每次用n除以2，商作为下一次的input，余数作为高位的结果，最先调用的函数的余数是最高位
"""
def intTobin0(n):
    """ non optimal """
    res = []
    if n == 0:
        return '0'
    while n != 0:
        remainder = n % 2
        res.append(str(remainder))
        n //= 2
    return ''.join(res[::-1])


def intTobin(n):
    """ 实现逆序输出，只不过前面会多一个0，借助这个0作为base condition向上返回过程中添加顶层的输出，
    实现了后调用的函数的返回值在前面，厉害厉害，有助于再次理解递归的过程
    """
    if n == 0:  # 输入为0的情况，也是base condition
        return '0'
    result = intTobin(n // 2)  # 注意这两行，先把子调用过程的结果拿到
    return result + str(n % 2)  # 返回的时候，把子过程的结果放在前面，再加上该函数自己的返回结果


# 之前还在想如何把逆序的结果输出来，搞了个res[::-1]，非常不好，递归天然是可以支持顺序的定义的
print(intTobin0(10))
print(intTobin0(3))

print(intTobin(10))
print(intTobin(3))
