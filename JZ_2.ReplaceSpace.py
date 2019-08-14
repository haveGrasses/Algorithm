class Solution:
    """ 统计空格的个数，定义一个新list，长度为原字符串的长度+空格个数*2，
    两个指针i，j从后向前扫，依次向新数组补数
    为啥要从后向前扫：
    """
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

    def replaceSpace2(self, s):
        """从前往后扫也没毛病"""
        numSpace = 0
        for i in s:
            if i == ' ':
                numSpace += 1
        newStr = ['' for _ in range(len(s)+numSpace*2)]
        i, j = 0, 0
        while i < len(s):
            if s[i] != ' ':
                newStr[j] = s[i]
                i += 1
                j += 1
            else:
                newStr[j] = '%'
                j += 1
                newStr[j] = '2'
                j += 1
                newStr[j] = '0'
                j += 1
                i += 1
        return ''.join(newStr)


print(Solution().replaceSpace('u jko l p'))

