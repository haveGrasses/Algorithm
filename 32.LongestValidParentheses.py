class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or not stack:  # 所有的(都是潜在的不合法元素；当stack为空时，所有的元素都是不合法的
                stack.append(i)
            elif s[i] == ')' and s[stack[-1]] == '(':  # 出现的)可以解救上一个不合法的(
                stack.pop()
            else:
                stack.append(i)  # 如果上一个并不是(，则当前的这个)也是不合法的

        if not stack:
            return len(s)

        # 这里之所以从后往前扫可能也是考虑到stack是从最后的开始出的性质吧，如果要从前往后扫，把start初值设为-1
        end, length = len(s), 0  # 注意这里end是len(s): end记录的是不合法的位置，不能从len(s)-1开始记，因为len(s)-1对应的可能是合法的
        while stack:
            start = stack.pop()
            length = max(length, end-start-1)
            end = start
        length = max(end, length)
        return length


s = Solution()
print(s.longestValidParentheses(")()())"))
