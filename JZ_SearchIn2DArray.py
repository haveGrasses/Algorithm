# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array) == 0  or len(array[0]) == 0:
            return False
        row, col = 0, len(array[0])-1
        while row < len(array) and col >= 0:
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                row += 1
            else:
                col -= 1
        return False
