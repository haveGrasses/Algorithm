class Solution:
    def isValid(self, s):
        stack = []  # using list as a stack
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in ')]}':  # len(stack) < 1: no opener was found; not in ['()', '[]', '{}']: cannot be pair
                if len(stack) < 1 or stack.pop() + i not in ['()', '[]', '{}']:
                    return False
        return len(stack) == 0  # or stack == []


# why using stack: nesting relations, the most recent found opener should be firstly paired
# the first found opener should be lastly paired.
# 栈顶元素表示在嵌套层次关系中最近的需要匹配的元素


class Solution2:
    """只考虑opener，push opener对应的closer而不是opener，简化判断条件"""
    def isValid(self, s):
        stack = []  # using list as a stack
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            else:  # found closer
                if stack == [] or stack.pop() != i:
                    return False
        return stack == []


class Solution3:
    """ Solution2将opener的每种情况进行if判断，当opener较多的时候有些冗长，可借助字典记录配对情况"""
    def isValid(self, s):
        stack = []  # using list as a stack
        pair_dict = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in pair_dict.keys():
                stack.append(pair_dict[i])
            else:
                if stack == [] or stack.pop() != i:  
                    return False
        return stack == []


class Solution4:
    """ Solution2将opener的每种情况进行if判断，当opener较多的时候有些冗长，可借助字典记录配对情况"""
    def isValid(self, s):
        stack = []  # using list as a stack
        pair_dict = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in pair_dict.values():
                stack.append(i)
            else:
                if stack == [] or stack.pop() != pair_dict[i]:  
                    return False
        return stack == []
