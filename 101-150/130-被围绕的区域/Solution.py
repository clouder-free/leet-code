#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二维的矩阵，包含'X'和'O'（字母 O）。
找到所有被'X'围绕的区域，并将这些区域里所有的'O'用'X'填充。
示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的'O'都不会被填充为'X'。
任何不在边界上，或不与边界上的'O'相连的'O'最终都会被填充为'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""

class Solution(object):

    def bfs(self, r, c, square, t):
        # t == 1边缘填充， t == 0中央填充
        nearr = [-1, 0, 1, 0]
        nearc = [0, 1, 0, -1]
        if square[r][c] != "O": return
        if t == 1:
            square[r][c] = "M"
        elif t == 0:
            square[r][c] = "X"
        for i in range(4):
            if r + nearr[i] >= 0 and r + nearr[i] < len(square) and c + nearc[i] >= 0 and c + nearc[i] < len(square[0]):
                self.bfs(r + nearr[i], c + nearc[i], square, t)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        elif board[0] == []:
            return

        # 首先，将边缘的O进行标记，标记为M
        for i in range(len(board[0])):
            if board[0][i] == "O":
                self.bfs(0, i, board, 1)
        for i in range(len(board[0])):
            if board[len(board) - 1][i] == "O":
                self.bfs(len(board) - 1, i, board, 1)
        for i in range(len(board)):
            if board[i][0] == "O":
                self.bfs(i, 0, board, 1)
        for i in range(len(board)):
            if board[i][len(board[0]) - 1] == "O":
                self.bfs(i, len(board[0]) - 1, board, 1)

        # 检查中间的连通区域
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "O":
                    self.bfs(i, j, board, 0)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "M":
                    board[i][j] = "O"


def main():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]]
    solution = Solution()
    solution.solve(board=board)

if __name__ == "__main__":
    main()

