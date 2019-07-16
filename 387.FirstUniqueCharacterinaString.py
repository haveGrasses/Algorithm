class Solution:
    """ hash """
    def firstUniqChar(self, s: str) -> int:
        cnt = {}
        for i in s:
            if i in cnt:
                cnt[i] = 2
            else:
                cnt[i] = 1
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1
