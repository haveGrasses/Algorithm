# 关于二进制的应用：
# 与运算&的作用：1. 清零；2. 取一个数中指定位，如x & 1：取x的个位
# 按位并：|, 把指定位数置为1
# 右移：101 >> 1 = 10; 把低位减少一位；左移: 101 << 1: 1010, 在低位增加一位
# 如何在循环中同时保存两种状态，但是不实际改变状态，
# 循环计算完成后再执行一次循环将每个对象做位移即可执行实际的改变，并且将高位腾出存放下一次结果

# 初始化都为0，只考虑填充为1的cell（极大地简化了原rule的4个条件）
# 如何处理扫描过程中边界点无法组成8个格子的越界问题


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # find lives in 3*3 boxes(or less consider border) centered on i, j
                lives = 0  # initiate

                # find neighbor box
                for x in range(max(0, i-1), min(i+2, m)):  # row 
                    for y in range(max(0, j-1), min(j+2, n)):  # col
                        lives += (board[x][y] & 1)  # lives += board[i][j]

                # apply rules: just consider when next state will be 1, and set other to 0, this is done by >>
                # lives == 3: whatever board[i][j] is, when lives == 3, next state is 1
                # lives - board[i][j] == 3: when board[i][j] == 1,  
                # the cell is to be still alive only when num of neighbors must be 3
                # ?? why use 'lives - board[i][j]' rather than 'lives - board[i][j] & 1' ??? 
                # fixed: use lives - (board[i][j]&1), brackets required
                if lives == 3 or lives - (board[i][j]&1) == 3:
                    board[i][j] |= 0b10  # set next state equal to 1

        for i in range(m):
            for j in range(n):
                # perform actual change
                board[i][j] >>= 1


testList = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s = Solution()
s.gameOfLife(testList)
print(testList)
