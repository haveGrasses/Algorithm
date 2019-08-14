class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        numSpace = 0
        for i in s:
            if i == ' ':
                numSpace += 1
        newStr = ['' for _ in range(len(s)+numSpace*2)]
        i, j = len(s) - 1, len(newStr) - 1
        while i >= 0:
            if s[i] != ' ':
                newStr[j] = s[i]
                i -= 1
                j -= 1
            else:
                newStr[j] = '0'
                j -= 1
                newStr[j] = '2'
                j -= 1
                newStr[j] = '%'
                j -= 1
                i -= 1
        return ''.join(newStr)


print(Solution().replaceSpace('u jko l p'))
