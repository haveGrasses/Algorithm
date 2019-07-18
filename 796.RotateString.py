class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        cur = A
        for i in range(len(A)):
            if cur == B:
                return True
            cur = cur[1:] + cur[0]
        return False

