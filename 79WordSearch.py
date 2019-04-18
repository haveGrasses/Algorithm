
class Solution(object):
    def exist(self, board, word):
        """ horizontally search """
        for i in range(len(board)):
            for j in range(len(board[0])):
                # this two loop determines i,j board[i][j] id the start point of search
                # first determine a start point, then search deeper in this given start point
                # if this start point fails, turn to another start point
                if self.dfs(board, i, j, word):
                    return True
        return False  # all direction fails

    def dfs(self, board, i, j, word):
        """ make sure whether there exists a path of given word start from board[i][j]
        this is dfs search!!!
        1. first check if board[i][j] == word[0], return false if not, turn to another direction in exist function
        2. recursively check the rest part of word, if not, turn to step 3
        3. turn to another direction in dfs (total 4 directions), return false if all direction fail
        :param i: row index
        :param j: col index
        :param word: target word
        :return: True or False
        """
        # check if board[i][j] == word[0]
        if len(word) == 0:
            return True
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 \
                or board[i][j] != word[0]:
            return False
        # word[0] and board[i][j] matched, check the rest part of word: decide whether this path can lead to all match
        tmp = board[i][j]
        board[i][j] = '#'  # avoid repeat use
        # if one direction return true, res is true
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
              or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp  # reset board[i][j]
        return res
