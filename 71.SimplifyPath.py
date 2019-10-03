class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for i in p:
            if i == '..':
                stack.pop()
            elif i and i != '.':
                stack.append(i)
        return '/' + '/'.join(stack)
