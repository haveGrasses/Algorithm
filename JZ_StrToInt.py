class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        intmap = dict((str(i), i) for i in range(10))  # dict(zip([str(i) for i in range(10)], [i for i in range(10)]))
        isNegative = s[0] == '-'
        ret = 0
        for i in range(len(s)):
            c = s[i]
            if i == 0 and (c == '+' or c == '-'):
                continue
            if c < '0' or c > '9':  # illegal input: '$' < '0', 'a' > '9'
                return 0
            ret = ret * 10 + intmap[c]
        return -1*ret if isNegative else ret
