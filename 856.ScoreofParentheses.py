class Solution0:
    """ 有点难懂，stack和cur在每个点对应的意思不太明白 """
    def scoreOfParentheses(self, S: str) -> int:
        stack, cur = [], 0
        for i in S:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)  # 当上一个cur是0时，这层结束的分数是1，否则变为两倍
        return cur


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for i in S:
            if i == '(':
                stack.append(-1)
            else:
                cur = 0
                while stack[-1] != -1:
                    cur += stack.pop()
                stack.pop()
                stack.append(1 if cur == 0 else cur * 2)
        res = 0
        while stack:
            res += stack.pop()
        return res


class Solution2:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for i in S:
            if i == '(':
                stack.append(-1)
            else:
                cur = 0
                while stack[-1] != -1:
                    cur += stack.pop()
                stack.pop()
                stack.append(1 if cur == 0 else cur * 2)
        return sum(stack)


S = '(()(()))'
S2 = '()()'
print(Solution2().scoreOfParentheses(S2))
