class Solution:
    def isValid(self, s: 'str') -> 'bool':
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