class Solution:
    def LeftRotateString(self, s, index):
        s = list(s)
        if len(s) == 0:
            return
        self.reverse(s, 0, index)
        self.reverse(s, index+1, len(s)-1)
        self.reverse(s, 0, len(s)-1)
        return ''.join(s)
    
    def RightRotateString(self, s, index):
        s = list(s)
        if len(s) == 0:
            return
        
        self.reverse(s, index, len(s)-1)
        self.reverse(s, 0, index-1)
        self.reverse(s, 0, len(s)-1)
        
        return ''.join(s)
        
    def reverse(self, s, start, end):
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1


s = Solution()
print(s.LeftRotateString('abcde', 1))
print(s.RightRotateString('abcde', 1))
